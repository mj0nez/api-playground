from fastapi import APIRouter

users_router = APIRouter()


@users_router.get("/users")
async def get_users() -> dict[str, str | int]:
    return {"a": "foo", "b": "bar", "c": 1}
