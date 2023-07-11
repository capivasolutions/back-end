from fastapi import FastAPI
from src.modules.transactions import transactions_router
from src.config import Database

app = FastAPI()
app.include_router(transactions_router)
Database.get_instance()
