from typing import Any

from fastapi import APIRouter, Depends, Request, Response
from fastapi.responses import JSONResponse
from fastapi.security import HTTPAuthorizationCredentials
from fastapi.security.http import HTTPBearer
from sqlalchemy.orm import Session

from general.ormbase import get_db
from workers.models.workers import Worker
from workers.schemas.workers_input import WorkerInput, WorkerInputPartial
from workers.schemas.workers_output import IncorrectWorkers, MultipleWorkersOutput, WorkerOutput

api_router = APIRouter()


@api_router.post("/", responses={200: {"model": WorkerOutput}})
def create_worker(
    request: Request,
    response: Response,
    input: WorkerInput,
    db: Any = Depends(get_db),
    auth: HTTPAuthorizationCredentials = Depends(HTTPBearer(auto_error=False)),
) -> WorkerOutput | IncorrectWorkers:
    """Create a new worker"""
    with db as sess:
        assert isinstance(sess, Session)
        worker = Worker(
            name=input.name,
            code=input.code,
            phone=input.phone,
            email=input.email,
            location=input.location,
        )
        sess.add(worker)
        sess.commit()
        sess.refresh(worker)
        return WorkerOutput(
            id=worker.id,
            name=worker.name,
            code=worker.code,
            phone=worker.phone,
            email=worker.email,
            location=worker.location,
        )


@api_router.get("/", responses={200: {"model": MultipleWorkersOutput}})
def get_worker(
    request: Request,
    response: Response,
    db: Any = Depends(get_db),
    auth: HTTPAuthorizationCredentials = Depends(HTTPBearer(auto_error=False)),
) -> MultipleWorkersOutput:
    with db as sess:
        assert isinstance(sess, Session)
        workers = sess.query(Worker).all()
        workersList = [
            WorkerOutput(
                id=worker.id,
                name=worker.name,
                code=worker.code,
                phone=worker.phone,
                email=worker.email,
                location=worker.location,
            )
            for worker in workers
        ]
        return MultipleWorkersOutput(workers=workersList)


@api_router.get(
    "/{worker_id}",
    responses={
        200: {"model": WorkerOutput},
        404: {"model": IncorrectWorkers},
    },
)
def get_specific_worker(
    request: Request,
    response: Response,
    worker_id: int,
    db: Any = Depends(get_db),
    auth: HTTPAuthorizationCredentials = Depends(HTTPBearer(auto_error=False)),
) -> WorkerOutput:
    with db as sess:
        assert isinstance(sess, Session)
        worker = sess.query(Worker).filter(Worker.id == worker_id).first()
        if worker is None:
            return JSONResponse(IncorrectWorkers(detail="Worker not found").json(), status_code=404)
        return WorkerOutput(
            id=worker.id,
            name=worker.name,
            code=worker.code,
            phone=worker.phone,
            email=worker.email,
            location=worker.location,
        )


@api_router.put(
    "/{worker_id}",
    responses={
        200: {"model": WorkerOutput},
        404: {"model": IncorrectWorkers},
    },
)
def update_worker(
    request: Request,
    response: Response,
    worker_id: int,
    input: WorkerInputPartial,
    db: Any = Depends(get_db),
    auth: HTTPAuthorizationCredentials = Depends(HTTPBearer(auto_error=False)),
) -> WorkerOutput | IncorrectWorkers:
    with db as session:
        worker = session.query(Worker).filter(Worker.id == worker_id).first()
        if worker is None:
            return JSONResponse(IncorrectWorkers(detail="Worker not found").json(), status_code=404)
        worker.name = input.name if input.name is not None else worker.name
        worker.code = input.code if input.code is not None else worker.code
        worker.phone = input.phone if input.phone is not None else worker.phone
        worker.email = input.email if input.email is not None else worker.email
        worker.location = input.location if input.location is not None else worker.location
        session.commit()
        return WorkerOutput(
            id=worker.id,
            name=worker.name,
            code=worker.code,
            phone=worker.phone,
            email=worker.email,
            location=worker.location,
        )
