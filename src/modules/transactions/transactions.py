from uuid import UUID
from enum import Enum
from typing import Union
from pydantic import BaseModel
from datetime import datetime


class TransactionClassification(str, Enum):
    FRAUDULENT = 'FRAUDULENT'
    GENUINE = 'GENUINE'


class Transaction(BaseModel):
    id: Union[UUID, None] = None
    time: float
    v1: float
    v2: float
    v3: float
    v4: float
    v5: float
    v6: float
    v7: float
    v8: float
    v9: float
    v10: float
    v11: float
    v12: float
    v13: float
    v14: float
    v15: float
    v16: float
    v17: float
    v18: float
    v19: float
    v20: float
    v21: float
    v22: float
    v23: float
    v24: float
    v25: float
    v26: float
    v27: float
    v28: float
    amount: float
    created_at: Union[datetime, None] = None
    updated_at: Union[datetime, None] = None
    classification: Union[TransactionClassification, None] = None

    def to_dict(self):
        return {
            'time': self.time,
            'v1': self.v1,
            'v2': self.v2,
            'v3': self.v3,
            'v4': self.v4,
            'v5': self.v5,
            'v6': self.v6,
            'v7': self.v7,
            'v8': self.v8,
            'v9': self.v9,
            'v10': self.v10,
            'v11': self.v11,
            'v12': self.v12,
            'v13': self.v13,
            'v14': self.v14,
            'v15': self.v15,
            'v16': self.v16,
            'v17': self.v17,
            'v18': self.v18,
            'v19': self.v19,
            'v20': self.v20,
            'v21': self.v21,
            'v22': self.v22,
            'v23': self.v23,
            'v24': self.v24,
            'v25': self.v25,
            'v26': self.v26,
            'v27': self.v27,
            'v28': self.v28,
            'amount': self.amount,
        }

    def __str__(self):
        return 'Transaction [ id: {}, amount: {}, classification: {}, created_at: {} ]'.format(str(self.id), self.amount, self.classification, self.created_at)
