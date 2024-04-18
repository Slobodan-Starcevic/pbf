import time
import string
import itertools
import sys

data_list = ["pass"]


def target_function(target_password):
    cracked_password = None
    possible_characters = string.ascii_letters + string.digits
    base = len(possible_characters)
    max_length = 15

    while not cracked_password:
        for length in range(1, max_length+1):
            for guess in itertools.product(possible_characters, repeat=length):
                if ''.join(guess) == target_password:
                    cracked_password = ''.join(guess)
                    break
                elif length == max_length+1:
                    break