from src.config import Logger
from src.modules.transactions.transactions import Transaction
from src.modules.transactions.transactions_repository import TransactionsRepository


class TransactionsService:
    def __init__(self) -> None:
        self.logger = Logger.get_instance()
        self.transaction_repository = TransactionsRepository()

    def create_transaction(self, transaction: Transaction) -> Transaction:
        self.logger.debug('Creating transaction {}'.format(transaction))
        self.transaction_repository.create_one(transaction)
        self.logger.debug('Transaction created {}'.format(transaction))
        return transaction
