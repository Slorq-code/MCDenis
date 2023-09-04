from pydantic import BaseModel, Field


class LoginOutput(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    token: str = Field(...)


class IncorrectLogin(BaseModel):
    detail: str = Field(...)
