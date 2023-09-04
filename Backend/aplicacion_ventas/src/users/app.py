from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_auth_middleware import AuthMiddleware

from general.auth import TokenVerificationBackend, auth_failure
from users.api.api import api_router

app = FastAPI(
    title="Aplicacion Ventas",
    description="Aplicacion para la gestion de ventas",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
)
app.include_router(api_router)
t = TokenVerificationBackend()

app.add_middleware(
    AuthMiddleware,
    verify_header=t.verify_authorization_header,
    excluded_urls=["/users/docs", "/users/redoc", "/users/openapi.json", "/users/login"],
    auth_error_handler=auth_failure,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
