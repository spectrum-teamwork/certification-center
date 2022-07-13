from fastapi import FastAPI
from sqladmin import Admin

from app import admin as a
from app.api import router
from app.database import engine
from app.settings import settings
from app.models import Base


app = FastAPI() if settings.debug is True else FastAPI(docs_url=None, redoc_url=None)
app.include_router(router)