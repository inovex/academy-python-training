class WizardingItem:

    def __init__(self, name: str, price: int, stock: int):
        self.name = name
        self.price = price
        self.stock = stock

    def sell(self, mum_items: int):
        if self.stock - mum_items < 0:
            raise OutOfStockError
        
        self.stock -= mum_items
        return mum_items * self.price

class OutOfStockError(Exception):
    pass

  