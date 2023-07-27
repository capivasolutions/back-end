from fastapi import APIRouter
from datetime import datetime
from uuid import UUID

from .transactions_service import TransactionsService
from .transactions import Transaction

transactions_service = TransactionsService()
transactions_router = APIRouter(
    prefix="/transactions",
    tags=["transactions"],
    responses={404: {"description": "Not found"}}
)


@transactions_router.post("/")
async def create_transaction(transaction: Transaction):
    transactions_service.create_transaction(transaction)
    return transaction


@transactions_router.get("/")
async def get_transactions(start_date: datetime = datetime.now()):
    transactions = transactions_service.get_transactions(start_date)
    return transactions


@transactions_router.get("/{id}")
async def get_transaction(id: UUID, limit: int = 100):
    transaction, transactions_to_compare = transactions_service.get_transaction(
        id, limit)
    return {"transaction": transaction, "comparable": transactions_to_compare}
