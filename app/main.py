from fastapi import FastAPI

from app import admin as a
from app.api import router
from app.database import engine
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
