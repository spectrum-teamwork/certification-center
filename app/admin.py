from turtle import title
from typing import ClassVar
import wtforms
from sqladmin import ModelAdmin, widgets

from app import models as m


class NewsAdmin(ModelAdmin, model=m.News):
    name: ClassVar[str] = "Новость"
    name_plural: ClassVar[str] = "Новости"

    column_list = [m.News.title, m.News.created_at]
    form_excluded_columns = [m.News.created_at, m.News.updated_at]
    form_overrides = dict(text=wtforms.TextAreaField)

    can_export = False


class ServiceAdmin(ModelAdmin, model=m.Service):
    name: ClassVar[str] = "Услуга"
    name_plural: ClassVar[str] = "Услуги"

    column_list = [m.Service.title, m.Service.service_type, m.Service.price]
    column_labels = dict(title="Оглавление", service_type="Тип сервиса", price="Стоимость услуги")

    # Creating
    form_args = dict(title=dict(description="Описание"))
    form_overrides = dict(description=wtforms.TextAreaField, requirements=wtforms.TextAreaField)
    form_excluded_columns = [m.Service.created_at, m.Service.updated_at]

    can_export = False


class ContactAdmin(ModelAdmin, model=m.Contact):
    name: ClassVar[str] = "Контакт"
    name_plural: ClassVar[str] = "Контакты"

    column_list = [m.Contact.city, m.Contact.address]
    form_overrides = dict(email=wtforms.EmailField)
    form_excluded_columns = [m.Contact.created_at, m.Contact.updated_at]

    can_export = False


class ClientAdmin(ModelAdmin, model=m.Client):
    name: ClassVar[str] = "Клиент"
    name_plural: ClassVar[str] = "Клиенты"

    column_list = [m.Client.title]
    form_excluded_columns = [m.Client.created_at, m.Client.updated_at]

    can_export = False


class CertificateAdmin(ModelAdmin, model=m.Certificate):
    name: ClassVar[str] = "Сертификат"
    name_plural: ClassVar[str] = "Сертификаты"

    column_list = [m.Certificate.label]
    form_excluded_columns = [m.Certificate.created_at, m.Certificate.updated_at]

    can_export = False


class AccreditationInfoAdmin(ModelAdmin, model=m.AccreditationInfo):
    name: ClassVar[str] = "Аккредитация"
    name_plural: ClassVar[str] = "Аккредитации"

    column_list = [m.AccreditationInfo.title]
    form_overrides = dict(text=wtforms.TextAreaField)

    can_create = False
    can_delete = False
    can_export = False


class ImagesAdmin(ModelAdmin, model=m.Image):
    column_list = [m.Image.id, m.Image.name]
    form_excluded_columns = [m.Contact.created_at, m.Contact.updated_at]

    can_export = False


class EmailAdmin(ModelAdmin, model=m.EmailConfig):
    name: ClassVar[str] = "Конфигурация email рассылки"
    name_plural: ClassVar[str] = "Настройки Email"
    column_list = [m.EmailConfig.MAIL_USERNAME, m.EmailConfig.MAIL_SERVER, m.EmailConfig.MAIL_PORT]

    can_delete = False
    can_export = False