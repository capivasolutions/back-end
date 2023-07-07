from fastapi import FastAPI
from src.routers import transactions

app = FastAPI()
app.include_router(transactions.router)
