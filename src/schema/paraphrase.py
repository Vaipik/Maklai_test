from pydantic import BaseModel


class TreeBase(BaseModel):
    query: str


class TreeResponse(BaseModel):
    response: list[str]
