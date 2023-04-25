from fastapi import APIRouter
from starlette import status

from src.schema.healtcheck import HealthCheck


healtcheck_router = APIRouter(
    prefix='/healtcheck',
    tags=["Healtcheck"]
)


@healtcheck_router.get(
    "/",
    response_model=HealthCheck,
    status_code=status.HTTP_200_OK
)
def ping_pong():
    return {"status": 200}
