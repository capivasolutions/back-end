from config import Environment, Database
from modules.transactions import transactions_router

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Backend service",
    description="Handle transactions",
    version="1.0.0",
    contact=None,
    license_info=None,
    terms_of_service=None,
)
app.add_middleware(CORSMiddleware, allow_origins=["*"])
app.include_router(transactions_router)


if __name__ == '__main__':
    Database.get_instance()
    uvicorn.run("main:app", host=Environment.BACKEND_HOST,
                port=Environment.BACKEND_PORT, reload=True)
