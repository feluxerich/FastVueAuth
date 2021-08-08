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

    # can be generated using: openssl rand -hex 32
    SECRET_KEY = environ.get('SECRET_KEY', "d2ee02d535a98e64e04716959aa42de641b8c0f33a9a5eb3a4d1e58add26ce49")
    ALGORITHM = environ.get('ALGORITHM', "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES = int(environ.get('ACCESS_TOKEN_EXPIRE_MINUTES', "10"))



settings = Settings()
