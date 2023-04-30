from fastapi import APIRouter

from src.services.paraphrase.main import paraphrase

paraphrase_router = APIRouter(
    prefix="/paraphrase",
    tags=["Paraphrase"]
)


@paraphrase_router.get("")
def paraphrase(tree: str, limit: int = 20):
    return paraphrase(tree)
