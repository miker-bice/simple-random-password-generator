import random
import string


def generate_random_pass(size):
    letters = string.ascii_letters
    digits = string.digits
    random_pass = "".join(random.choices(letters + digits, k=size))
    return random_pass
