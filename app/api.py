
from fastapi import APIRouter, BackgroundTasks, Depends, File, UploadFile
from fastapi.responses import Response
from fastapi_mail import FastMail, MessageSchema
from pydantic import UUID4
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app import crud
from app import models as m
from app import schemas as s
from app.database import get_db
from app.settings import email_conf

router = APIRouter(prefix='/api/v1')


@router.get('/main/title', response_model=s.TitleInfoOut, tags=['main'])
async def get_title_info(db: AsyncSession = Depends(get_db)):
    """Получить описание на главной странице."""
    return await crud.read_title_info(db)


@router.get('/main/contacts', response_model=list[s.ContactsOut], tags=['main'])
async def get_contacts(db: AsyncSession = Depends(get_db)):
    """Получить список контактов."""
    return await crud.read_contacts(db)


@router.get('/services', response_model=list[s.ServiceOut], tags=['services'])
async def get_all_services(db: AsyncSession = Depends(get_db)):
    """Получить список всех услуг."""
    return await crud.read_services(db)


@router.get('/clients', response_model=list[s.ClientOut], tags=['clients'])
async def get_all_clients(db: AsyncSession = Depends(get_db)):
    """Получить всех клиентов."""
    return await crud.read_clients(db)


@router.get('/accreditation/info', response_model=s.AccreditationInfoOut, tags=['accreditation'])
async def get_accreditation_info(db: AsyncSession = Depends(get_db)):
    """Получить описание аккредитаций."""
    return await crud.read_accreditation_info(db)


@router.get('/accreditation/certificates', response_model=list[s.CertsOut], tags=['accreditation'])
async def get_accreditation_certificates(db: AsyncSession = Depends(get_db)):
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


@router.get('/news', response_model=list[s.NewsOut], tags=['news'])
async def get_all_news(db: AsyncSession = Depends(get_db)):
    """Получить список всех новостей."""
    return await crud.read_all_news(db)


@router.get('/news/{news_id}', response_model=s.NewsFullOut, tags=['news'])
async def get_news_by_id(news_id: UUID4, db: AsyncSession = Depends(get_db)):
    """Получить список всех новостей."""
    return await crud.read_news_by_id(news_id, db)


@router.get('/orders', response_model=list[s.OrderOut], response_model_exclude_none=True)
async def get_all_orders(db: AsyncSession = Depends(get_db)):
    """ВРЕМЕННО!"""
    stmt = await db.execute(select(m.Order))
    return stmt.scalars().all()


def make_message(order: s.OrderIn) -> str:
    html = f"""
    <h2>Создана новая заявка</h2>
    <p>Контактное лицо: {order.contact_name}</p>
    <p>Телефон: {order.phone}</p>
    <p>Электронная почта: {order.email}</p>
    <p>Комментарий: {order.comment}</p>
    """
    return html


@router.post('/orders/order', status_code=202, tags=['orders'])
async def create_order( order: s.OrderIn, background_tasks: BackgroundTasks, db: AsyncSession = Depends(get_db)):
    """Создать заявку..."""
    # Запись в БД
    stmt = await crud.create_order(order, db)
    await db.commit()
    await db.refresh(stmt)
    
    # db_service = await crud.read_service_by_id(order.service_id, db)
    # db_contact = await crud.read_contact_by_id(order.region, db)

    # Рассылка писем
    fm = FastMail(email_conf)
    message = MessageSchema(subject="Новая заявка!", recipients=['yarlistratenko@yandex.ru'], html=make_message(order))
    background_tasks.add_task(fm.send_message, message)

    return {'message': 'order was created', 'order_id': stmt.id}
