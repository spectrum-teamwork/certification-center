from fastapi_mail import ConnectionConfig
from pydantic import BaseSettings, EmailStr


class Settings(BaseSettings):
    database: str
    debug: bool

    class Config:
        env_file = '.env'


class EmailSettings(BaseSettings):
    MAIL_USERNAME: str
    MAIL_PASSWORD: str
    MAIL_FROM: EmailStr
    MAIL_PORT: int
    MAIL_SERVER: str
    MAIL_FROM_NAME: str
    MAIL_TLS: bool
    MAIL_SSL: bool
    USE_CREDENTIALS: bool
    VALIDATE_CERTS: bool

    class Config:
        env_file = '.env'


settings = Settings()
email_conf = ConnectionConfig(**EmailSettings().dict())
