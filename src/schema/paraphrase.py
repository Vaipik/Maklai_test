from pydantic import BaseModel


class TreeBase(BaseModel):
    tree: str


class TreeResponse(BaseModel):
    response: list[str]
