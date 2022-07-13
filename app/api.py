from re import L
from sqlalchemy import select, update
from fastapi import APIRouter, Depends, File, Form, UploadFile
from fastapi.responses import Response
from pydantic import UUID4
from sqlalchemy.ext.asyncio import AsyncSession

from app import crud
from app import models as m
from app import schemas as s
from app.database import get_db

router = APIRouter(prefix='/api/v1')


@router.get('/services', response_model=list[s.ServiceOut], tags=['services'])
async def get_all_services(db: AsyncSession = Depends(get_db)):
    """Получить список всех услуг."""
    return await crud.read_services(db)


@router.post('/services/service', status_code=201, tags=['services'])
async def create_service(service: s.ServiceIn, db: AsyncSession = Depends(get_db)):
    """Создать услугу."""
    stmt = m.Service(**service.dict())
    db.add(stmt)
    await db.commit()


@router.get('/clients', response_model=list[s.ClientOut], tags=['clients'])
async def get_all_clients(db: AsyncSession = Depends(get_db)):
    """Получить всех клиентов."""
    return await crud.read_clients(db)


@router.get('/accreditation/info', response_model=s.AccreditationInfoOut, tags=['accreditation'])
async def get_accreditation_info(db: AsyncSession = Depends(get_db)):
    """Получить описание аккредитаций."""
    return await crud.read_accreditation_info(db)


@router.get('/accreditation/certeficates', response_model=list[s.CertsOut], tags=['accreditation'])
async def get_accreditation_certeficates(db: AsyncSession = Depends(get_db)):
    """Получить описание аккредитаций."""
    return await crud.read_certificates(db)


@router.get('/images/{image_id}', tags=['images'])
async def get_image(image_id: UUID4, db: AsyncSession = Depends(get_db)):
    """Получить изображение."""
    result = await crud.read_image(image_id, db)
    return Response(content=result.data, media_type="image/png")


@router.post('/images/image', status_code=201, tags=['images'])
async def upload_file_on_server(image: UploadFile = File(..., media_type='image/png'), db: AsyncSession = Depends(get_db)):
    """Загрузить изображение."""
    stmt = m.Image(name=image.filename, data=image.file.read())
    db.add(stmt)
    await db.commit()
    await db.refresh(stmt)
    return {'detail': 'images was added', 'image_id': stmt.id}
