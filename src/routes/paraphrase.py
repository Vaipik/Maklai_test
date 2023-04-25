from fastapi import APIRouter

from src.schema.paraphrase import TreeBase


paraphrase_router = APIRouter(
    prefix="/paraphrase",
    tags=["Paraphrase"]
)


@paraphrase_router.get("/")
def paraphrase(query_tree: TreeBase):
    pass
