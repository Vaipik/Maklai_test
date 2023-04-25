from fastapi import APIRouter


healtcheck_router = APIRouter(
    prefix='/healtcheck',
    tags=["Healtcheck"]
)


@healtcheck_router.get("/")
def ping_pong():
    return {"status": "OK"}
