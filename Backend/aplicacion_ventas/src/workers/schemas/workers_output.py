from typing import Optional

from pydantic import BaseModel, Field


class WorkerOutput(BaseModel):
    id: int = Field(..., ge=1)
    name: str = Field(..., min_length=3, max_length=90)
    code: str = Field(..., min_length=3, max_length=45)
    phone: str = Field(..., min_length=3, max_length=20)
    email: str = Field(..., min_length=3, max_length=90)

    # optional fields

    location: Optional[str] = Field(None, min_length=3, max_length=255)


class MultipleWorkersOutput(BaseModel):
    workers: list[WorkerOutput]


class IncorrectWorkers(BaseModel):
    detail: str = Field(..., min_length=3, max_length=90)
