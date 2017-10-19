from cashflow.util.Shop import Shop


class MUFGShop(Shop):

    def __init__(self, text):
        super().__init__(text)
        self.original_name = text
        self.clean_name = MUFGShop.cleanup(text)
        self.filter = MUFGShop.create_filter(text)

    @staticmethod
    def create_filter(text):
        tmptxt = text
        if "PAYPAL *" in tmptxt:
            return tmptxt[0:tmptxt.rfind("/")].strip()
        return tmptxt

    @staticmethod
    def cleanup(text):
        tmptxt = text
        if "PAYPAL *" in tmptxt:
            tmptxt = tmptxt[8:]
            tmptxt = tmptxt[0:tmptxt.rfind("/")].strip()
        return tmptxt
