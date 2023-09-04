from typing import Any

from fastapi import APIRouter, Depends, Request, Response
from fastapi.responses import JSONResponse
from fastapi.security import HTTPAuthorizationCredentials
from fastapi.security.http import HTTPBearer
from sqlalchemy.orm import Session

from general.auth import TokenVerificationBackend
from general.ormbase import get_db
from users.models.users import User
from users.schemas.user_input import LoginInput
from users.schemas.user_output import IncorrectLogin, LoginOutput

api_router = APIRouter()


@api_router.post("/login", responses={200: {"model": LoginOutput}, 401: {"model": IncorrectLogin}})
def login(
    request: Request,
    response: Response,
    input: LoginInput,
    db: Any = Depends(get_db),
) -> LoginOutput | IncorrectLogin:
    """Login"""
    with db as sess:
        assert isinstance(sess, Session)
        user = sess.query(User).filter(User.username == input.username).first()
        if user is None:
            return JSONResponse(IncorrectLogin(detail="Incorrect username or password").json(), status_code=401)
        assert isinstance(user, User)
        valido = user.check_password(input.password)
        if not valido:
            return JSONResponse(IncorrectLogin(detail="Incorrect username or password").json(), status_code=401)
        back = TokenVerificationBackend()
        token = back.generate_token(user)
        return LoginOutput(username=user.username, token=token)


@api_router.get("/me", responses={200: {"model": LoginOutput}, 401: {"model": IncorrectLogin}})
def me(
    request: Request,
    response: Response,
    db: Session = Depends(get_db),
    auth: HTTPAuthorizationCredentials = Depends(HTTPBearer(auto_error=False)),
) -> LoginOutput:
    """Get the current user"""
    return LoginOutput(username=request.user, token=auth.credentials)
