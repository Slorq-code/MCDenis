import os

from fastapi.testclient import TestClient
from sqlalchemy_utils import create_database, database_exists

from app import app
from general.ormbase import Base, ORMManager, ORMTesting
from users.models.users import User
from workers.models.workers import Worker

os.environ["MYSQL_DATABASE"] = "aplicacion_ventas_test"


SQLALCHEMY_DATABASE_URL = ORMTesting()._get_db_url()

test_client = TestClient(app)


class TestWorkers:
    token = None

    def create_database(self):
        if not database_exists(ORMTesting()._get_db_url()):
            create_database(ORMTesting()._get_db_url())

    def setup_method(self):
        # we create the database from ORMTestin
        self.create_database()
        Base.metadata.create_all(ORMTesting().engine)
        user = User(username="testa", password="testtest", is_superuser=True)
        with ORMManager.get_orm(ORMTesting)._get_session() as db:
            db.add(user)
            db.commit()
        response = test_client.post("/users/login", json={"username": "testa", "password": "testtest"})
        assert response.status_code == 200
        self.token = response.json()["token"]

    def teardown_method(self):
        Base.metadata.drop_all(ORMTesting().engine)

    def test_create_worker_wrong_name(self):
        response = test_client.post(
            "/workers/",
            json={"name": "na", "code": "code", "phone": "phone", "email": "a@gmail.com"},
            headers={"Authorization": f"Bearer {self.token}"},
        )
        assert response.status_code == 422

    def test_create_worker_correct(self):
        response = test_client.post(
            "/workers/",
            json={"name": "na", "code": "code", "phone": "phone", "email": "a@gmail.com"},
            headers={"Authorization": f"Bearer {self.token}"},
        )
        assert response.status_code == 422

    def test_get_single_worker(self):
        worker = Worker(name="name", code="code", phone="phone", email="a@gmail.com")
        with ORMManager.get_orm(ORMTesting)._get_session() as db:
            db.add(worker)
            db.commit()
        response = test_client.get("/workers/1", headers={"Authorization": f"Bearer {self.token}"})
        assert response.status_code == 200
        assert response.json()["name"] == "name"
        assert response.json()["code"] == "code"
        assert response.json()["phone"] == "phone"
        assert response.json()["email"] == "a@gmail.com"

    def test_get_single_worker_wrong_id(self):
        response = test_client.get("/workers/1", headers={"Authorization": f"Bearer {self.token}"})
        assert response.status_code == 404

    def test_get_all_workers(self):
        worker = Worker(name="name", code="code", phone="phone", email="@gmail.com")
        with ORMManager.get_orm(ORMTesting)._get_session() as db:
            db.add(worker)
            db.commit()
        response = test_client.get("/workers/", headers={"Authorization": f"Bearer {self.token}"})
        assert response.status_code == 200
        workers = response.json()["workers"]
        assert len(workers) == 1
        assert workers[0]["name"] == "name"
        assert workers[0]["code"] == "code"
        assert workers[0]["phone"] == "phone"
        assert workers[0]["email"] == "@gmail.com"

    def test_get_all_workers_empty(self):
        response = test_client.get("/workers/", headers={"Authorization": f"Bearer {self.token}"})
        assert response.status_code == 200
        workers = response.json()["workers"]
        assert len(workers) == 0

    def test_update_worker(self):
        worker = Worker(name="name", code="code", phone="phone", email="a@gmail.com")
        with ORMManager.get_orm(ORMTesting)._get_session() as db:
            db.add(worker)
            db.commit()
        response = test_client.put(
            "/workers/1",
            json={
                "name": "name2",
                "code": "code2",
                "phone": "phone2",
            },
            headers={"Authorization": f"Bearer {self.token}"},
        )
        assert response.status_code == 200
        assert response.json()["name"] == "name2"
        assert response.json()["code"] == "code2"
        assert response.json()["phone"] == "phone2"
        assert response.json()["email"] == "a@gmail.com"
        response = test_client.get("/workers/1", headers={"Authorization": f"Bearer {self.token}"})
        assert response.status_code == 200
        assert response.json()["name"] == "name2"
        assert response.json()["code"] == "code2"
        assert response.json()["phone"] == "phone2"
        assert response.json()["email"] == "a@gmail.com"
