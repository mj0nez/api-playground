from fastapi import APIRouter

from playground.models import pydantic

users_router = APIRouter()


@users_router.post("/users")
async def get_users() -> dict[str, str | int]:
    return {"a": "foo", "b": "bar", "c": 1}

# for consistency and simplifying testing we keep the pydantic prefix
# although, there is no other validation and parsing library 
interactions_router = APIRouter(prefix="/interactions")


@interactions_router.post("/pydantic")
async def post_interaction_pydantic(data: pydantic.Interactions) -> str:
    return "hi"


@interactions_router.post("/pydantic/roundtrip")
async def post_interaction_pydantic_with_serialization(
    data: pydantic.Interactions,
) -> pydantic.Interactions:
    return data
