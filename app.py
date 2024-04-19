def index_converter(index):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    base = len(chars)
    result = ""

    while index > 0:
        remainder = index % base
        result = chars[remainder] + result
        index = index // base

    return result


index = 87587
combination = index_converter(index)
print(combination)
