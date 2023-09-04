from typing import Optional

from pydantic import BaseModel, Field


class WorkerInput(BaseModel):
    name: str = Field(..., min_length=3, max_length=90)
    code: str = Field(..., min_length=3, max_length=45)
    phone: str = Field(..., min_length=3, max_length=20)
    email: str = Field(..., min_length=3, max_length=90)

    # optional fields

    location: Optional[str] = Field(None, min_length=3, max_length=255)


class WorkerInputPartial(BaseModel):
    name: Optional[str] = Field(None, min_length=3, max_length=90)
    code: Optional[str] = Field(None, min_length=3, max_length=45)
    phone: Optional[str] = Field(None, min_length=3, max_length=20)
    email: Optional[str] = Field(None, min_length=3, max_length=90)
    location: Optional[str] = Field(None, min_length=3, max_length=255)
