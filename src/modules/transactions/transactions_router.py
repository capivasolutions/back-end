from fastapi import APIRouter
from src.modules.transactions.transactions_service import TransactionsService
from src.modules.transactions.transactions import Transaction

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
