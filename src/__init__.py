from fastapi import FastAPI

from .routes import healtcheck_router, paraphrase_router


def init_app(app: FastAPI) -> FastAPI:
    app.include_router(healtcheck_router)
    app.include_router(paraphrase_router)
    return app
