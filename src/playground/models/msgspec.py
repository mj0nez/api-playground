import msgspec


class User(msgspec.Struct):
    id: int
    name: str
    age: int


class Repo(msgspec.Struct):
    name: str


class Actor(msgspec.Struct):
    login: str


class Interaction(msgspec.Struct):
    actor: Actor
    repo: Repo


class Interactions(msgspec.Struct):
    interactions: list[Interaction]
