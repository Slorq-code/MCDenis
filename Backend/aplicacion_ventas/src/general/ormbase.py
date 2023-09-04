import os
from abc import abstractmethod
from contextlib import contextmanager
from typing import Any, Generator, Iterator, Optional, Type

from sqlalchemy import create_engine, engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.orm.decl_api import as_declarative
from sqlalchemy.pool import NullPool, StaticPool


@as_declarative()
class Base:
    """Base class for all models"""

    pass


class ORMBase:
    """Base class for all models"""

    base = Base

    def __init__(self, pool: bool = True, eng_params: dict | None = None):
        if eng_params is None:
            eng_params = {}
        self._sess_mkr: sessionmaker | None = None
        self._engine: engine.Engine | None = None
        self._pool = pool
        self._eng_params = eng_params
        self._scoped_session = None

    @abstractmethod
    def _get_db_url(self) -> str:
        """Returns the database url"""
        raise NotImplementedError

    def _create_engine(self) -> None:
        eng_params = {
            "poolclass": NullPool if not self._pool else StaticPool,
            "pool_pre_ping": True,
            "pool_recycle": 30,
        }
        eng_params = {**eng_params, **self._eng_params}
        self._engine = create_engine(self._get_db_url(), **eng_params)  # type: ignore

    def _create_session_mkr(self) -> None:
        if self._engine is None:
            self._create_engine()
        assert self._engine is not None
        self._sess_mkr = sessionmaker(bind=self._engine)

    def _get_engine(self) -> engine.Engine:
        if self._engine is None:
            self._create_engine()
        assert self._engine is not None
        return self._engine

    def _get_session(self) -> sessionmaker:
        if self._sess_mkr is None:
            self._create_session_mkr()
        assert self._sess_mkr is not None
        return self._sess_mkr()

    def _get_scoped_session(self) -> scoped_session:
        if self._sess_mkr is None:
            self._create_session_mkr()

        return scoped_session(self._sess_mkr)  # type: ignore

    @contextmanager
    def session(self) -> Iterator:
        sess = None
        try:
            sess = self._get_scoped_session()
            yield sess
            sess.commit()
        except Exception:
            if sess is not None:
                sess.rollback()
            raise
        finally:
            if sess is not None:
                sess.close()
                del sess

    @property
    def engine(self) -> Optional[engine.Engine]:
        return self._get_engine()


class ORMDefault(ORMBase):
    def _get_db_url(self) -> str:
        protocol = "mysql+pymysql"
        username = os.environ.get("MYSQL_USER", "app")
        password = os.environ.get("MYSQL_PASSWORD", "password")
        host = os.environ.get("MYSQL_HOST", "localhost")
        port = os.environ.get("MYSQL_PORT", "3306")
        db_name = os.environ.get("MYSQL_DATABASE", "aplicacion_ventas")

        return f"{protocol}://{username}:{password}@{host}:{port}/{db_name}"


class ORMTesting(ORMDefault):
    def _get_db_url(self) -> str:
        protocol = "mysql+pymysql"
        username = os.environ.get("MYSQL_USER", "app")
        password = os.environ.get("MYSQL_PASSWORD", "password")
        host = os.environ.get("MYSQL_HOST", "localhost")
        port = os.environ.get("MYSQL_PORT", "3306")
        db_name = "aplicacion_ventas_test"

        return f"{protocol}://{username}:{password}@{host}:{port}/{db_name}"


class ORMManager:
    ORMS: list = []

    @staticmethod
    def get_orm(orm_class: Type[ORMBase] = ORMDefault, **kwargs: Any) -> ORMBase:
        for orm in ORMManager.ORMS:
            if orm["name"] != orm_class.__name__:
                continue
            skip = False

            for karg in kwargs:
                if karg not in orm or orm[karg] != kwargs[karg]:
                    skip = True
                    break

            if skip:
                continue

            return orm["orm"]

        orm = orm_class(**kwargs)

        ORMManager.ORMS.append({"name": orm_class.__name__, "orm": orm, **kwargs})

        return orm


def get_db() -> Generator[sessionmaker, Any, None]:
    try:
        db = ORMManager.get_orm()._get_session()
        yield db
    except Exception:
        raise
    finally:
        if db is not None:
            db.close()  # type: ignore
            del db
