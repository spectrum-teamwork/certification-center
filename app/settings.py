from pydantic import BaseSettings


class Settings(BaseSettings):
    database: str
    debug: bool
    
    class Config:
        env_file = '.env'


settings = Settings()