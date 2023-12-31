from datetime import datetime
from typing import List
from uuid import UUID
from fastapi.exceptions import HTTPException

from modules.classifications.classifier_service import ClassifierService
from config import Logger
from .transactions import Transaction, TransactionClassification
from .transactions_repository import TransactionsRepository


class TransactionsService:
    def __init__(self) -> None:
        self.logger = Logger.get_instance()
        self.repository = TransactionsRepository()
        self.classifier = ClassifierService()

    def create_transaction(self, transaction: Transaction) -> Transaction:
        classification = self.classifier.classify(transaction)
        transaction.classification = classification

        self.logger.debug(f'Creating transaction {transaction}')
        self.repository.create_one(transaction)
        self.logger.debug(f'Transaction created {transaction}')

        return transaction

    def get_transactions(self, start_date: datetime) -> List[Transaction]:
        self.logger.debug(f'Getting all transactions from {start_date}')
        transactions = self.repository.get_many(start_date)
        self.logger.debug(
            f'Found {len(transactions)} transactions from {start_date}')
        return transactions

    def get_transaction(self, id: UUID, limit: int) -> (Transaction, List[Transaction]):
        self.logger.debug(f'Getting transaction by id {id}')
        transaction = self.repository.get_one(id)

        if transaction is None:
            self.logger.debug(f'Transaction {id} does not exist')
            raise HTTPException(404, f'Transaction {id} does not exist')

        transactions_to_compare = []
        if transaction.classification == TransactionClassification.FRAUDULENT:
            self.logger.debug(f'Getting genuine transactions to compare')
            fraudulent_transactions = self.repository.get_many_by_class(
                TransactionClassification.GENUINE, limit)
            transactions_to_compare.extend(fraudulent_transactions)
        else:
            self.logger.debug(f'Getting fraudulent transactions to compare')
            genuine_transactions = self.repository.get_many_by_class(
                TransactionClassification.FRAUDULENT, limit)
            transactions_to_compare.extend(genuine_transactions)

        return transaction, transactions_to_compare
