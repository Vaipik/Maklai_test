from pydantic import BaseModel, Field


class HealthCheck(BaseModel):
    status: int = Field(default=200)
