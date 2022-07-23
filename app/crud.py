from pydantic import UUID4
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app import models as m
from app import schemas as s


async def read_title_info(db: AsyncSession):
    stmt = await db.execute(select(m.TitleInfo))
    return stmt.scalar_one_or_none()


async def read_contacts(db: AsyncSession):
    stmt = await db.execute(select(m.Contact))
    return stmt.scalars().all()


async def read_contact_by_id(contact_id: UUID4, db: AsyncSession):
    stmt = await db.execute(select(m.Contact).where(m.Contact.id == contact_id))
    return stmt.scalar_one_or_none()


async def read_services(db: AsyncSession):
    stmt = await db.execute(select(m.Service))
    return stmt.scalars().all()


async def read_service_by_id(service_id: UUID4, db: AsyncSession):
    stmt = await db.execute(select(m.Service).where(m.Service.id == service_id))
    return stmt.scalar_one_or_none()


async def read_clients(db: AsyncSession):
    stmt = await db.execute(select(m.Client))
    return stmt.scalars().all()


async def read_accreditation_info(db: AsyncSession):
    stmt = await db.execute(select(m.AccreditationInfo))
    return stmt.scalar_one()


async def read_certificates(db: AsyncSession):
    stmt = await db.execute(select(m.Certificate))
    return stmt.scalars().all()


async def read_image(image_id: UUID4, db: AsyncSession):
    """Получить изображение."""
    stmt = select(m.Image).where(m.Image.id == image_id)
    result = await db.execute(stmt)
    return result.scalar_one()


async def read_all_news(db: AsyncSession):
    stmt = await db.execute(select(m.News))
    return stmt.scalars().all()


async def read_news_by_id(news_id: UUID4, db: AsyncSession):
    stmt = await db.execute(select(m.News).where(m.News.id == news_id))
    return stmt.scalar_one()


async def create_order(order: s.OrderIn, db: AsyncSession):
    stmt = m.Order(**order.dict(exclude_unset=True))
    db.add(stmt)
    return stmt
