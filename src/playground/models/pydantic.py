from pydantic import BaseModel


class Repo(BaseModel):
    name: str


class Actor(BaseModel):
    login: str


class Interaction(BaseModel):
    actor: Actor
    repo: Repo


class Interactions(BaseModel):
    interactions: list[Interaction]
