class Integer:
    def __init__(self, value):
        self.value = value

    @staticmethod
    def from_float(float_value):
        if not isinstance(float_value, float):
            return "value is not a float"
        return Integer(int(float_value))

    @staticmethod
    def from_roman(value):
        def value_(r):
            if r == 'I':
                return 1
            if r == 'V':
                return 5
            if r == 'X':
                return 10
            if r == 'L':
                return 50
            if r == 'C':
                return 100
            if r == 'D':
                return 500
            if r == 'M':
                return 1000
            return -1

        def romanToDecimal(str):
            res = 0
            i = 0

            while i < len(str):

                s1 = value_(str[i])

                if i + 1 < len(str):
                    s2 = value_(str[i + 1])
                    if s1 >= s2:
                        res = res + s1
                        i = i + 1
                    else:
                        res = res + s2 - s1
                        i = i + 2
                else:
                    res = res + s1
                    i = i + 1

            return Integer(int(res))

        return romanToDecimal(value)

    @staticmethod
    def from_string(value):
        if str(value).isdigit():
            return Integer(int(value))
        else:
            return "wrong type"

