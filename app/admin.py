from app import models as m
from sqladmin import ModelAdmin
from sqladmin import widgets
import wtforms


class NewsAdmin(ModelAdmin, model=m.News):
    column_list = [m.News.title, m.News.text, m.News.image_id]


class ServiceAdmin(ModelAdmin, model=m.Service):
    column_list = [m.Service.title, m.Service.service_type, m.Service.price]

    column_labels = {m.Service.title: "Оглавление"}

    # Creating
    form_columns = [m.Service.title, m.Service.service_type, m.Service.description,
                    m.Service.price, m.Service.image_id, m.Service.image_document_id]
    form_args = {'title': {'label': 'Оглавление'}}
    form_widget_args = {'price': {'model': widgets.TimePickerWidget}}
    from_overrides = {m.Service.image_id: wtforms.FileField}

    can_export = False


class ContactAdmin(ModelAdmin, model=m.Contact):
    column_list = [m.Contact.id, m.Contact.city, m.Contact.address]


class ClientAdmin(ModelAdmin, model=m.Client):
    column_list = [m.Client.id, m.Client.title]


class CertificateAdmin(ModelAdmin, model=m.Certificate):
    column_list = [m.Certificate.id, m.Certificate.label]


class AccreditationInfoAdmin(ModelAdmin, model=m.AccreditationInfo):
    column_list = [m.AccreditationInfo.id,
                   m.AccreditationInfo.title, m.AccreditationInfo.text]

    can_create = False


class ImagesAdmin(ModelAdmin, model=m.Image):
    column_list = [m.Image.id, m.Image.name]