from fastapi import APIRouter

router = APIRouter(
    prefix="/transactions",
    tags=["transactions"],
    responses={404: {"description": "Not found"}}
)


@router.get("/")
async def get_transactions():
    return [{"id": 1, "amount": "19.99", "isFraud": False}, {"id": 2, "amount": "29.99", "isFraud": True}]


@router.get("/{id}")
async def get_transaction(id: str):
    return {"id": 1, "amount": "19.99", "isFraud": False}
