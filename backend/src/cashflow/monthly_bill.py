import datetime


class MonthlyBill:

    @property
    def pay_date(self):
        return self._pay_date

    @property
    def billing_month(self):
        return self._billing_month.month

    @property
    def billing_year(self):
        return self._billing_month.year

    def __init__(self):
        self._pay_date = datetime.datetime.now()
        self._billing_month = datetime.datetime.now()

