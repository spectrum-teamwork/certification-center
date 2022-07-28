from pydantic import UUID4, BaseModel, EmailStr, validator
from app.models import ServiceTypes


class TitleInfoOut(BaseModel):
    title: str
    text: str

    class Config:
        orm_mode = True
        
    @validator('title', 'text', pre=True)
    def dump_text(cls, v: str):
        return v.replace('\n', '<br>')


class ContactsOut(BaseModel):
    id: UUID4
    region: str
    city: str
    address: str
    phone: str
    email: str
    place_src: str

    class Config:
        orm_mode = True


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
        
    @validator('title', 'requirements', 'description', pre=True)
    def dump_text(cls, v: str):
        return v.replace('\n', '<br>')


class ClientIn(BaseModel):
    title: str
    image_id: UUID4 | None


class ClientOut(ClientIn):
    id: UUID4

    class Config:
        orm_mode = True


class CertsOut(BaseModel):
    id: UUID4
    label: str
    image_id: UUID4 | None

    class Config:
        orm_mode = True


class AccreditationInfoOut(BaseModel):
    title: str
    text: str

    class Config:
        orm_mode = True


class NewsFullOut(BaseModel):
    id: UUID4
    title: str
    text: str
    image_id: UUID4 | None

    class Config:
        orm_mode = True


class NewsOut(NewsFullOut):
    @validator('text', pre=True)
    def dump_text(cls, v: str):
        return ' '.join(v.split(' ')[:14]) + ' ...'


class OrderIn(BaseModel):
    contact_id: UUID4
    service_id: UUID4 | None
    contact_name: str | None
    phone: str | None
    email: EmailStr | None
    comment: str | None


class OrderOut(OrderIn):
    id: UUID4

    class Config:
        orm_mode = True
