def is_digit(string):
    if string.isdigit():
        return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False


def int_whether_float(num):
    num = float(num)
    if num.is_integer():
        return int(num)
    return num
