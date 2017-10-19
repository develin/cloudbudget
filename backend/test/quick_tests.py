import logging
from cashflow.mufg.mufg_card import MUFGCard


def main():
    try:
        card = MUFGCard.from_file(r"C:\Users\benfr\OneDrive\Documents\CreditCard\201608.csv")
        logging.getLogger(__name__).info("Done")
    except Exception as ex:
        logging.getLogger(__name__).critical("Failed to parse file due to {}".format(ex))


logging.basicConfig()
if __name__ == "__main__":
    main()

