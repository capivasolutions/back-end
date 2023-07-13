import random
from src.config import Logger
from src.modules.transactions.transactions import Transaction, TransactionClassification


class TransactionsClassifierService:
    def __init__(self) -> None:
        self.logger = Logger.get_instance()

    def classify(self, transaction: Transaction) -> TransactionClassification:
        self.logger.debug(f'Classifying transaction {transaction}')

        # TODO: integrate to IA Model
        classification = random.randint(0, 1)
        if classification == 0:
            self.logger.debug(
                f'Transaction {transaction} classified as {TransactionClassification.FRAUDULENT}')
            return TransactionClassification.FRAUDULENT
        else:
            self.logger.debug(
                f'Transaction {transaction} classified as {TransactionClassification.GENUINE}')
            return TransactionClassification.GENUINE
