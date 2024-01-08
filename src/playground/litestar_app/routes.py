from litestar import Controller, get, post

from playground.litestar_app.dto import (
    InteractionsMsgSpecDTO,
    InteractionsPydanticDTO,
    UserDTO,
)
from playground.models import msgspec, pydantic


@get("/sample")
async def get_sample() -> dict[str, str | int]:
    return {"a": "foo", "b": "bar", "c": 1}


# dto type will automatically be used for the return type
@post("/users", dto=UserDTO)
async def get_user(data: msgspec.User) -> msgspec.User:
    return data


class InteractionsController(Controller):
    path: str = "/interactions"

    @post("/msgspec", dto=InteractionsMsgSpecDTO, return_dto=None)
    async def post_interaction_msgspec(self, data: msgspec.Interactions) -> str:
        return "hi"

    @post("/pydantic", dto=InteractionsPydanticDTO, return_dto=None)
    async def post_interaction_pydantic(self, data: pydantic.Interactions) -> str:
        return "hi"
