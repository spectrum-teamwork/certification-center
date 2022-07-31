from fastapi import FastAPI
from sqlalchemy import select

from app import admin as a
from app import models as m
from app.api import router
from app.database import async_session, engine
from app.settings import settings

app = FastAPI() if settings.debug is True else FastAPI(docs_url=None, redoc_url=None)


admin = a.MyAdmin(app, engine)
admin.register_model(a.TitleAdmin)
admin.register_model(a.NewsAdmin)
admin.register_model(a.ServiceAdmin)
admin.register_model(a.ContactAdmin)
admin.register_model(a.ClientAdmin)
admin.register_model(a.CertificateAdmin)
admin.register_model(a.AccreditationInfoAdmin)
admin.register_model(a.ImagesAdmin)
admin.register_model(a.EmailAdmin)

app.include_router(router)


@app.on_event("startup")
async def startup_event():
    async with async_session() as db:
        stmt = await db.execute(select(m.TitleInfo))
        dat = stmt.scalar_one_or_none()
        if dat is None:
            db.add(m.TitleInfo(title='Заголовок', text='Текст'))
            await db.commit()
            
        stmt = await db.execute(select(m.AccreditationInfo))
        dat = stmt.scalar_one_or_none()
        if dat is None:
            db.add(m.AccreditationInfo(title='Заголовок', text='Текст'))
            await db.commit()
