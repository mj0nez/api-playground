from litestar.contrib.pydantic import PydanticDTO
from litestar.dto import DTOConfig, MsgspecDTO

from playground.models import msgspec, pydantic


class UserDTO(MsgspecDTO[msgspec.User]):
    pass


class InteractionsMsgSpecDTO(MsgspecDTO[msgspec.Interactions]):
    # we have to add this depth as we have the following nesting levels:
    # 0: Interactions, 1: Interaction, 2: Actor/Repo
    # if we omit this config a max depth of 1 is set and our requests fail
    # more or less silently with a generic 500: Internal server error
    config = DTOConfig(max_nested_depth=2)


class InteractionsPydanticDTO(PydanticDTO[pydantic.Interactions]):
    # we have to add this depth as we have the following nesting levels:
    # 0: Interactions, 1: Interaction, 2: Actor/Repo
    # if we omit this config a max depth of 1 is set and our requests fail
    # more or less silently with a generic 500: Internal server error
    config = DTOConfig(max_nested_depth=2)
