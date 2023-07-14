import random
from src.config import Logger
from src.modules.transactions.transactions import Transaction, TransactionClassification
import MPL
import torch
import numpy as np
from torch.autograd import Variable

class TransactionsClassifierService:
    def __init__(self) -> None:
        self.logger = Logger.get_instance()
        self.model = torch.load('./modelo.pth')
        self.model.eval() # This makes the normal behaviour be predict and not learn

    def classify(self, transaction: Transaction) -> TransactionClassification:
        self.logger.debug(f'Classifying transaction {transaction}')

        # Taking the required data to make the prediction
        data = [[
                 Transaction.v3,
                 Transaction.v4,
                 Transaction.v5,
                 Transaction.v7,
                 Transaction.v9,
                 Transaction.v10,
                 Transaction.v11,
                 Transaction.v12,
                 Transaction.v14,
                 Transaction.v16,
                 Transaction.v17,
                 Transaction.v19,
                 Transaction.amount
                ]]

        # Turning data into a Variable for pytorch
        entry = Variable(torch.from_numpy(data)).float()

        # Classifying the entry
        classification = self.model(entry)

        # Finally extracting the predicted class
        classification = classification.argmax().item()

        if classification == 1:
            self.logger.debug(
                f'Transaction {transaction} classified as {TransactionClassification.FRAUDULENT}')
            return TransactionClassification.FRAUDULENT
        else:
            self.logger.debug(
                f'Transaction {transaction} classified as {TransactionClassification.GENUINE}')
            return TransactionClassification.GENUINE
