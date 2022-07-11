from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from app.settings import settings

engine = create_async_engine(settings.database, echo=settings.debug)


async def get_db() -> AsyncSession:
    async_session = sessionmaker(engine, autocommit=False, autoflush=False, expire_on_commit=False, class_=AsyncSession)
    async with async_session() as session:
        yield session