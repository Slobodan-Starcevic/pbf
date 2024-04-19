
possible_characters = "abcdefghijklmnopqrstuvwxyz"
base = len(possible_characters)
max_length = 5
data_list = range(0, len(possible_characters)**max_length)
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

    return None
