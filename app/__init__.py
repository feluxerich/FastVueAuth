from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse

from app.config import settings
from app.database import SessionLocal, engine
from app.user import models
from app.user.router import router as user_router
from app.auth.router import router as auth_router

models.Base.metadata.create_all(bind=engine)


def create_app():
    app = FastAPI(
        title=settings.TITLE,
        description=settings.DESCRIPTION,
        version=settings.VERSION,
        debug=settings.DEBUG,
    )
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
        allow_credentials=True,
    )
    app.include_router(user_router, prefix=f"{settings.API_ROUTE}/user")
    app.include_router(auth_router, prefix=f"{settings.API_ROUTE}/auth")

    @app.get("/")
    async def root():
        return RedirectResponse(url='/docs')

    return app
