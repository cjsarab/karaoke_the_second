class Guest:
    def __init__(self, cash):
        self.cash = cash

    def buy_drink(self, drink):
        if drink.price <= self.cash:
            self.cash -= drink.price
