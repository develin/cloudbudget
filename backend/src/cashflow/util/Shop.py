class Shop:

    def __init__(self, text):
        self.original_name = text
        self.clean_name = Shop.cleanup(text)
        self.filter = Shop.create_filter(text)

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
