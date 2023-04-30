from typing import Optional

from pydantic import BaseModel


class TreeBase(BaseModel):
    tree: str


class TreeResponse(BaseModel):
    paraphrases: list[Optional[TreeBase]]
