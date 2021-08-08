from os import environ
from pydantic import BaseSettings


class Settings(BaseSettings):
    TITLE = environ.get("TITLE", "FastVueAuth")
    DESCRIPTION = environ.get("DESCRIPTION", "")
    VERSION = float(environ.get("VERSION", "0.1"))
    DEBUG = bool(int(environ.get("DEBUG", "0")))

    API_ROUTE = f"/api/v{int(VERSION)}"
    #SQLALCHEMY_DATABASE_URL = "sqlite:///database.sqlite"
    SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:root@localhost:3306/fva"


settings = Settings()
