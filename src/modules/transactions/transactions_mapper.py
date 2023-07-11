from src.modules.transactions.transactions import Transaction


class TransactionsMapper:
    def from_request(request: dict) -> Transaction:
        return Transaction(id=request['id'], time=request['time'], v1=request['v1'], v2=request['v2'], v3=request['v3'], v4=request['v4'], v5=request['v5'], amount=request['amount'], created_at=request['created_at'], updated_at=request['updated_at'], classification=request['class'])

    def from_database():
        raise NotImplementedError()
