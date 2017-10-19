import unicodedata

import datetime


class ShiftJISConverter(object):
    DELETE_STRING = ' "'

    def __init__(self):
        super()

    def convert(self, string):
        return unicodedata.normalize('NFKD', string).replace('"', '').strip()

    def convert_all(self, string_list):
        result = []
        for item in string_list:
            result.append(self.convert(item))
        return result

    def convert_to_float(self, string):
        tmp = self.convert(string)

    def convert_to_int(self, string):
        tmp = self.convert(string)
        result = 0
        digit = -1
        for letter in string:
            digit = unicodedata.digit(letter, -1)
            if digit >= 0:
                result = result * 10 + digit
        return result

    def convert_date(self, datestring):
        return datetime.date(self.convert_to_int(datestring[0:5]), self.convert_to_int(datestring[6:8]),
                             self.convert_to_int(datestring[8:]))
