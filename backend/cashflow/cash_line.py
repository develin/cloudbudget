from cashflow.util.Shop import Shop


class CashLine:

    def __init__(self):
        self.user = ""
        self.shop = ""
        self.payment_date = ""
        self.usage_date = ""
        self.payment_count = ""
        self.amount = 0

    @staticmethod
    def from_parameters(self, user, shop, payment_date, usage_date, payment_count, amount):
        self.user = user
        self.shop = Shop.cleanup(shop)
        self.payment_date = payment_date
        self.usage_date = usage_date
        self.payment_count = payment_count
        self.amount = amount

