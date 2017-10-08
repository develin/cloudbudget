class Shop:

    def __init__(self, text):
        self.original_name = text
        self.clean_name = Shop.cleanup(text)

    def get_clean_name(self):
        return self.clean_name

    @staticmethod
    def cleanup(text):
        tmptxt = text
        if "PAYPAL *" in tmptxt:
            tmptxt = tmptxt[8:]
            tmptxt = tmptxt[0:tmptxt.rfind("/")].strip()
        return tmptxt
