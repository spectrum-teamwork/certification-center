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
    form_columns = [m.Service.title, m.Service.service_type, m.Service.description, m.Service.price, m.Service.image_id, m.Service.image_document_id]
    form_args = {'title': {'label': 'Оглавление'}}
    form_widget_args = {'price': {'model': widgets.TimePickerWidget}}
    from_overrides = {m.Service.image_id: wtforms.FileField}

    can_export = False
