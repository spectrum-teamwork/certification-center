from pydantic import UUID4
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app import models as m
from app import schemas as s


async def read_services(db: AsyncSession):
    stmt = select(m.Service)
    result = await db.execute(stmt)
    return result.scalars().all()


async def read_clients(db: AsyncSession):
    stmt = select(m.Client)
    result = await db.execute(stmt)
    return result.scalars().all()


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
