from typing import ClassVar

import wtforms
from fastapi import HTTPException, Request, Response
from fastapi.responses import RedirectResponse
from sqladmin import Admin, ModelAdmin

from app import models as m
from app.database import async_session


class MyAdmin(Admin):
    async def create(self, request: Request) -> Response:
        """Create model endpoint."""

        await self._create(request)

        identity = request.path_params["identity"]
        model_admin = self._find_model_admin(identity)

        Form = await model_admin.scaffold_form()
        form = Form(await request.form())

        context = {
            "request": request,
            "model_admin": model_admin,
            "form": form,
        }

        if request.method == "GET":
            return self.templates.TemplateResponse(model_admin.create_template, context)

        if not form.validate():
            return self.templates.TemplateResponse(
                model_admin.create_template,
                context,
                status_code=400,
            )

        data = form.data
        if image := form.data.get('image_id'):
            if image.filename != '':
                async with async_session() as db:
                    stmt = m.Image(name=image.filename, data=image.file.read())
                    db.add(stmt)
                    await db.commit()
                    await db.refresh(stmt)

                data['image_id'] = str(stmt.id)
            else:
                del data['image_id']

        if image := form.data.get('image_document_id'):
            if image.filename != '':
                async with async_session() as db:
                    stmt = m.Image(name=image.filename, data=image.file.read())
                    db.add(stmt)
                    await db.commit()
                    await db.refresh(stmt)

                data['image_document_id'] = str(stmt.id)
            else:
                del data['image_document_id']

        model = model_admin.model(**data)
        await model_admin.insert_model(model)

        return RedirectResponse(
            request.url_for("admin:list", identity=identity),
            status_code=302,
        )

    async def edit(self, request: Request, ) -> Response:
        """Edit model endpoint."""

        await self._edit(request)

        identity = request.path_params["identity"]
        model_admin = self._find_model_admin(identity)

        model = await model_admin.get_model_by_pk(request.path_params["pk"])
        if not model:
            raise HTTPException(status_code=404)

        Form = await model_admin.scaffold_form()
        context = {
            "request": request,
            "model_admin": model_admin,
        }

        if request.method == "GET":
            context["form"] = Form(obj=model)
            return self.templates.TemplateResponse(model_admin.edit_template, context)

        form = Form(await request.form())
        if not form.validate():
            context["form"] = form
            return self.templates.TemplateResponse(
                model_admin.edit_template,
                context,
                status_code=400,
            )

        data = form.data

        if image := form.data.get('image_id'):
            if image.filename != '':
                async with async_session() as db:
                    stmt = m.Image(name=image.filename, data=image.file.read())
                    db.add(stmt)
                    await db.commit()
                    await db.refresh(stmt)

                data['image_id'] = str(stmt.id)
            else:
                del data['image_id']

        if image := form.data.get('image_document_id'):
            if image.filename != '':
                async with async_session() as db:
                    stmt = m.Image(name=image.filename, data=image.file.read())
                    db.add(stmt)
                    await db.commit()
                    await db.refresh(stmt)

                data['image_document_id'] = str(stmt.id)
            else:
                del data['image_document_id']
        await model_admin.update_model(pk=request.path_params["pk"], data=data)

        return RedirectResponse(
            request.url_for("admin:list", identity=identity),
            status_code=302,
        )


class NewsAdmin(ModelAdmin, model=m.News):
    name: ClassVar[str] = "Новость"
    name_plural: ClassVar[str] = "Новости"

    edit_template: ClassVar[str] = 'edit.html'
    create_template: ClassVar[str] = 'create.html'

    column_list = [m.News.title, m.News.created_at]
    form_excluded_columns = [m.News.created_at, m.News.updated_at]
    form_overrides = dict(text=wtforms.TextAreaField, image_id=wtforms.FileField)

    can_export = False


class ServiceAdmin(ModelAdmin, model=m.Service):
    name: ClassVar[str] = "Услуга"
    name_plural: ClassVar[str] = "Услуги"

    edit_template: ClassVar[str] = 'edit.html'
    create_template: ClassVar[str] = 'create.html'

    column_list = [m.Service.title, m.Service.service_type, m.Service.price]
    column_labels = dict(title="Оглавление", service_type="Тип сервиса", price="Стоимость услуги")

    # Creating
    form_args = dict(title=dict(description="Описание"))
    form_overrides = dict(description=wtforms.TextAreaField, requirements=wtforms.TextAreaField,
                          image_id=wtforms.FileField, image_document_id=wtforms.FileField)
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

    edit_template: ClassVar[str] = 'edit.html'
    create_template: ClassVar[str] = 'create.html'

    column_list = [m.Client.title]

    form_overrides = dict(image_id=wtforms.FileField)
    form_excluded_columns = [m.Client.created_at, m.Client.updated_at]

    can_export = False


class CertificateAdmin(ModelAdmin, model=m.Certificate):
    name: ClassVar[str] = "Сертификат"
    name_plural: ClassVar[str] = "Сертификаты"

    edit_template: ClassVar[str] = 'edit.html'
    create_template: ClassVar[str] = 'create.html'

    column_list = [m.Certificate.label]
    form_overrides = dict(image_id=wtforms.FileField)
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
