from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="AI Visit Timer")

app.include_router(router)
