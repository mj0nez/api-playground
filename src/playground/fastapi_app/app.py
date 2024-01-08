from fastapi import FastAPI

from playground.fastapi_app.routes import interactions_router, users_router

app = FastAPI(debug=True)

app.include_router(users_router)
app.include_router(interactions_router)
