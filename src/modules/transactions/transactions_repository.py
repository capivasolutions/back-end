import uuid
from uuid import UUID
from typing import List, Union
from datetime import datetime, timezone

from config import Logger, Database
from .transactions import Transaction, TransactionsMapper
from .transactions_queries import CREATE_ONE_TRANSACTION, GET_TRANSACTIONS_FROM_DATE, GET_TRANSACTION_BY_ID


class TransactionsRepository:
    def __init__(self) -> None:
        self.logger = Logger.get_instance()

    def create_one(self, transaction: Transaction) -> Transaction:
        connection = Database.get_instance()
        cursor = connection.cursor()
        try:
            id = str(transaction.id) if transaction.id is not None else str(
                uuid.uuid4())
            created_at = transaction.created_at if transaction.created_at is not None else datetime.now(
                timezone.utc)
            updated_at = transaction.updated_at if transaction.updated_at is not None else datetime.now(
                timezone.utc)
            cursor.execute(CREATE_ONE_TRANSACTION, (
                id, transaction.time, transaction.v1, transaction.v2, transaction.v3, transaction.v4, transaction.v5,
                transaction.v6, transaction.v7, transaction.v8, transaction.v9, transaction.v10, transaction.v11,
                transaction.v12, transaction.v13,
                transaction.v14, transaction.v15, transaction.v16, transaction.v17, transaction.v18, transaction.v19,
                transaction.v20, transaction.v21, transaction.v22, transaction.v23, transaction.v24, transaction.v25,
                transaction.v26, transaction.v27, transaction.v28, transaction.amount, transaction.classification,
                created_at, updated_at))
            connection.commit()
            return transaction
        except Exception as error:
            self.logger.error(error, 'Error while trying create transaction')
            raise error

    def get_many(self, start_date: datetime) -> List[Transaction]:
        connection = Database.get_instance()
        cursor = connection.cursor()
        try:
            cursor.execute(GET_TRANSACTIONS_FROM_DATE, (start_date,))
            transactions = cursor.fetchall()
            return list(map(lambda t: TransactionsMapper.to_model(t), transactions))
        except Exception as error:
            self.logger.error(error, 'Error while trying get transactions')
            raise error

    def get_one(self, id: UUID) -> Union[Transaction, None]:
        connection = Database.get_instance()
        cursor = connection.cursor()
        try:
            cursor.execute(GET_TRANSACTION_BY_ID, (str(id),))
            transaction = cursor.fetchone()
            if transaction is None:
                return None
            return TransactionsMapper.to_model(transaction)
        except Exception as error:
            self.logger.error(error, 'Error while trying get transactions')
            raise error
