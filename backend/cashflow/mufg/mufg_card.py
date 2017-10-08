from cashflow.cash_line import CashLine


class MUFGCard:
    SEPARATOR = ','

    def __init__(self):
        self.last_customer = ""
        self.rows = []
        return

    def __is_customer_name(self, tokens):
        user = ""
        count = 0
        for token in tokens:
            if len(token.strip()) == 0:
                count = count + 1
            else:
                user = token.strip()
        if count == 1:
            self.last_customer = user
            return True
        return False

    def parse_line(self, line):
        tokens = line.split(MUFGCard.SEPARATOR)
        if len(tokens) != 8 or self.__is_customer_name(tokens):
            return

        ''' "Confirmed information", "Payment date", "Your shop name (Overseas shop name / Overseas city name)", \
         "Date of use", "Number of payments", "How many times", "Amount spent (yen) ",\
         " Local currency amount · currency name · exchange rate " '''

        self.rows.append(CashLine.from_parameters(self, self.last_customer, tokens[2], tokens[1],
                                                   tokens[3], tokens[4], tokens[6]))

    @staticmethod
    def from_file(filename):
        card = MUFGCard()
        with open(filename, 'r') as f:
            card.parse_line(f.read())
        f.closed()
        return card

