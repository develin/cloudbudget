from cashflow.monthly_bill import MonthlyBill
from cashflow.mufg.MUFGShop import MUFGShop
from cashflow.util.shift_jis_converter import ShiftJISConverter
from src.cashflow.single_payment import SinglePayment
import unicodedata


class MUFGCard(MonthlyBill):
    SEPARATOR = ','

    def __init__(self):
        super().__init__()
        self.last_customer = ""
        self.rows = []
        self.convert = ShiftJISConverter()
        return

    @staticmethod
    def __clean_up_name(name):
        return ' '.join(list(reversed(name.replace('【', '').replace('】', '').replace('様', '').strip().split('　')))) \
            .strip()

    def __is_customer_name(self, tokens):
        user = ""
        count = 0
        for token in tokens:
            token = token.strip().replace('"', '').strip()
            if len(token) > 0:
                count = count + 1
                user = token
        if count == 1:
            self.last_customer = MUFGCard.__clean_up_name(user)
            return True
        return False

    def parse_line(self, line):
        tokens = line.split(MUFGCard.SEPARATOR)
        if not (len(tokens) in (8, 9)) or self.__is_customer_name(tokens):
            return

        if len(self.last_customer) == 0:
            return
        ''' "Confirmed information", "Payment date", "Your shop name (Overseas shop name / Overseas city name)", \
         "Date of use", "Number of payments", "How many times", "Amount spent (yen) ",\
         " Local currency amount · currency name · exchange rate " '''

        row = SinglePayment(user=self.last_customer, shop=MUFGShop(tokens[2]),
                            payment_date=self.convert.convert_date(tokens[1]),
                            usage_date=self.convert.convert_date(tokens[3]),
                            payment_count=self.convert.convert_to_int(tokens[4]),
                            amount=self.convert.convert_to_int(tokens[6]), description="")

        self.rows.append(row)

    @staticmethod
    def from_file(filename):
        card = MUFGCard()
        with open(filename, mode='r', encoding='shift_jis') as local_file:
            for line in local_file:
                card.parse_line(line)
        return card
