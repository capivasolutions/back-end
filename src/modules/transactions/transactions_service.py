from datetime import datetime
from typing import List
from src.config import Logger
from src.modules.transactions.transactions import Transaction
from src.modules.transactions.transactions_repository import TransactionsRepository
from src.modules.classifications import ClassifierService


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
