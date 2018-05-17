# Write a Python class to convert an integer to a roman numeral.


class Roman:
    """a class to convert integer to roman numeral


    """
    @staticmethod
    def int_to_roman(num):
        values = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        symbols = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]
        roman_num = ""
        i = 0
        while num > 0:
            for __ in range(num // values[i]):
                roman_num += symbols[i]
                num -= values[i]
            i += 1
        return roman_num


print(Roman.int_to_roman(2018))
