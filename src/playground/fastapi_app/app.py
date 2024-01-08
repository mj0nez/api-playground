import uvicorn
from fastapi import FastAPI

from playground.fastapi_app.routes import users_router

app = FastAPI()


app.include_router(users_router)


