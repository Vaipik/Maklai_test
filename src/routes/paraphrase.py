from fastapi import APIRouter

from src.schema.paraphrase import TreeResponse
from src.services.paraphrase import paraphrases

paraphrase_router = APIRouter(
    prefix="/paraphrase",
    tags=["Paraphrase"]
)


@paraphrase_router.get(
    "",
    response_model=TreeResponse
)
def paraphrase(tree: str, limit: int = 20):
    return paraphrases(tree, limit)
