from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    lm_studio_url: str
    lm_model: str

    class Config:
        env_file = ".env"


settings = Settings()