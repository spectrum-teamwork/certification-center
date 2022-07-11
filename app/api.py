from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import models as m

from app import crud
from app.database import get_db
from app import schemas as s

router = APIRouter(prefix='/api/v1')