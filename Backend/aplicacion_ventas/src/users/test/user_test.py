import os

from fastapi.testclient import TestClient
from sqlalchemy_utils import create_database, database_exists

from app import app
from general.ormbase import Base, ORMManager, ORMTesting
from users.models.users import User

os.environ["MYSQL_DATABASE"] = "aplicacion_ventas_test"


SQLALCHEMY_DATABASE_URL = ORMTesting()._get_db_url()

test_client = TestClient(app)


class TestLogin:
    def create_database(self):
        if not database_exists(ORMTesting()._get_db_url()):
            create_database(ORMTesting()._get_db_url())

    def setup_method(self):
        # we create the database fro ORMTesting
        self.create_database()
        Base.metadata.create_all(ORMTesting().engine)
        user = User(username="testa", password="testtest", is_superuser=True)
        with ORMManager.get_orm(ORMTesting)._get_session() as db:
            db.add(user)
            db.commit()

    def teardown_method(self):
        Base.metadata.drop_all(ORMTesting().engine)

    def test_login_fail_username(self):
        response = test_client.post("/users/login", json={"username": "testfail", "password": "testtest"})
        assert response.status_code == 401

    def test_login_fail_password(self):
        response = test_client.post("/users/login", json={"username": "testa", "password": "testfail"})
        assert response.status_code == 401

    def test_login_success(self):
        response = test_client.post("/users/login", json={"username": "testa", "password": "testtest"})
        assert response.status_code == 200
        token = response.json()["token"]
        response = test_client.get("/users/me", headers={"Authorization": f"Bearer {token}"})
        assert response.status_code == 200
