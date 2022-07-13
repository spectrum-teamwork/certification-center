from base64 import b64encode
from pydantic import UUID4, BaseModel, validator
from app.models import ServiceTypes


class ServiceIn(BaseModel):
    title: str
    service_type: ServiceTypes
    description: str
    requirements: str
    price: float


class ServiceOut(ServiceIn):
    id: UUID4
    image_id: UUID4
    image_document_id: UUID4

    class Config:
        orm_mode = True


class ClientIn(BaseModel):
    title: str
    image_id: UUID4 | None


class ClientOut(ClientIn):
    id: UUID4
