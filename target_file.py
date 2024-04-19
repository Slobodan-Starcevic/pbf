
possible_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
base = len(possible_characters)
max_length = 10
data_list = list(range(0, len(possible_characters)**10))
target_password = "passw"


# Algorithm that converts an index into its corresponding combination based on the chosen base system
def target_function(index):
    result = ''

    while index > 0:
        remainder = index % base
        result = possible_characters[remainder] + result
        index = index // base

    if result == target_password:
        return result
