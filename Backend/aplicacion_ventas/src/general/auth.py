import os
from datetime import datetime, timedelta

import jwt
from fastapi import HTTPException
from fastapi.requests import HTTPConnection
from fastapi.responses import JSONResponse
from starlette.authentication import AuthenticationError
from starlette.datastructures import Headers

from users.models.users import User


class TokenVerificationBackend:
    def __init__(self) -> None:
        self.secret_key = os.environ["SECRET_KEY"]
        self.algorithm = "HS256"

    def verify_authorization_header(self, auth_header: Headers) -> tuple[list[str], str]:
        """Verify the authorization header and return the scopes and username"""

        if "Authorization" not in auth_header:
            raise HTTPException(status_code=401, detail="Authorization header not found")
        token = auth_header["Authorization"].split(" ")[1]
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
        except jwt.exceptions.InvalidSignatureError:
            raise HTTPException(status_code=401, detail="Invalid token")
        except jwt.exceptions.DecodeError:
            raise HTTPException(status_code=401, detail="Invalid token")
        except jwt.exceptions.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail="Token expired")
        scopes = payload.get("scopes", [])
        if payload.get("is_superuser", None):
            scopes.append("superuser")
        return scopes, payload.get("username", "")

    def generate_token(self, user: User) -> str:
        """Generate a JWT token for the given user"""
        payload = {
            "user_id": user.id,
            "username": user.username,
            "is_superuser": user.is_superuser,
            "is_active": user.is_active,
            "exp": datetime.utcnow() + timedelta(minutes=120),
        }
        return jwt.encode(payload, self.secret_key, algorithm=self.algorithm)


def auth_failure(request: HTTPConnection, error: AuthenticationError) -> JSONResponse:
    """Return a JSON response for authentication failure"""
    return JSONResponse({"detail": "Unauthorized"}, status_code=401)
