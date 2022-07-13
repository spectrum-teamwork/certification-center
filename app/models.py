import enum
from datetime import datetime
from uuid import uuid4
from pydantic import UUID4

from sqlalchemy import TIMESTAMP, Boolean, Column, Enum, Float, String, func, LargeBinary
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base
from app.database import engine

Base = declarative_base()


class ServiceTypes(enum.Enum):
    TESTING = 'testing'
    CERTIFICATION = 'certification'


class IdMixin(Base):
    __abstract__ = True

    id = Column(UUID(as_uuid=True), primary_key=True, unique=True, index=True, default=uuid4)


class CreateUpdateMixin(Base):
    __abstract__ = True

    created_at = Column(TIMESTAMP, default=datetime.utcnow, server_default=func.now(), nullable=False)
    updated_at = Column(TIMESTAMP)


# class User(IdMixin, CreateUpdateMixin):
#     __tablename__ = 'users'

#     name = Column(String, nullable=False)

#     password_hash = Column(String, nullable=False)

#     full_name = Column(String)

#     email = Column(String, nullable=False)
#     phone = Column(String, nullable=False)

#     is_active = Column(Boolean, default=False, nullable=False)


class Service(IdMixin, CreateUpdateMixin):
    __tablename__ = 'services'

    title = Column(String, nullable=False)  # Название
    service_type = Column(Enum(ServiceTypes), nullable=False)  # Тип (Испытание или Сертификация)
    image_id = Column(UUID)  # Изображение для слайдера
    description = Column(String, nullable=False)  # Текст с описанием услуги (по сути текст статьи про услугу)
    image_document_id = Column(UUID)  # Пример выдаваемого документа (картинка)
    requirements = Column(String, nullable=False)  # Список требований для проведения испытаний (текст?) Возможно стоит сделать JSON list
    price = Column(Float, nullable=False)  # Стоимость работ - для всех регионов стоимость одинаковая (число)


class Client(IdMixin, CreateUpdateMixin):  # Клиенты
    __tablename__ = 'clients'

    title = Column(String)  # Название (текст)
    image_id = Column(UUID)  # Изображение PNG - 167х133


class Image(IdMixin, CreateUpdateMixin):
    __tablename__ = 'images'

    name = Column(String, nullable=False)
    data = Column(LargeBinary, nullable=False)


class AccreditationInfo(IdMixin):
    __tablename__ = 'accreditation_info'

    title = Column(String, nullable=False)  # Заголовок блок
    text = Column(String, nullable=False)  # Текст блокаа


class Certificate(IdMixin, CreateUpdateMixin):  # Аттестаты и аккредитация
    __tablename__ = 'certificates'

    label = Column(String, nullable=False)  # Подпись к изображению
    image_id = Column(UUID)  # Изображение 350х275


class News(IdMixin, CreateUpdateMixin):  # Новости
    __tablename__ = 'news'

    title = Column(String, nullable=False)
    image_id = Column(UUID)
    text = Column(String)
    

# class Contact(IdMixin, CreateUpdateMixin):
#     __tablename__ = 'contacts'


# class Order(IdMixin, CreateUpdateMixin):
#     __tablename__ = 'orders'

#     service_id = Column(UUID)
#     region = Column(String)

#     contact_name = Column(String)
#     phone = Column(String)
#     email = Column(String)
#     comment = Column(String)

#     is_consent = Column(Boolean, nullable=False)  # согласие на обработку


# Новости:
#  19. Постер (изображение) главное изображение к статье
#  20. Заголовок статьи
#  21. Текст статьи
#   Так же есть слайдер для списка новостей, должна быть возможность:
#     1. Получать список статей
#     2. Каждый элемент списка содержит id новости, Постер, название статьи (новости), краткий текст статьи (начало статьи обрезанное примерно до 14 первых слов)
