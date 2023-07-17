
import requests
from src.config import Logger, Environment
from src.modules.transactions.transactions import Transaction, TransactionClassification


class ClassifierService:
    def __init__(self) -> None:
        self.logger = Logger.get_instance()

    def classify(self, transaction: Transaction) -> TransactionClassification:
        self.logger.debug(f'Classifying transaction {transaction}')

        response = requests.post(
            Environment.CLASSIFIER_URL, json=transaction.to_dict())
        classification = response.json()['classification']

        if classification == TransactionClassification.FRAUDULENT:
            self.logger.debug(
                f'Transaction {transaction} classified as {TransactionClassification.FRAUDULENT}')
            return TransactionClassification.FRAUDULENT
        else:
            self.logger.debug(
                f'Transaction {transaction} classified as {TransactionClassification.GENUINE}')
            return TransactionClassification.GENUINE
