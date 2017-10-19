from cashflow.util.Shop import Shop


class SinglePayment:

    def __init__(self, user="", shop=None, payment_date="", usage_date="", payment_count="", amount=0, description=""):
        self.user = user
        self.shop = shop
        self.payment_date = payment_date
        self.usage_date = usage_date
        self.payment_count = payment_count
        self.amount = amount
        self.description = description

