import random

LOWER_LIMIT = 10_000_000_000_000
UPPER_LIMIT = 99_999_999_999_999

def generate_pk():
    return random.randint(LOWER_LIMIT, UPPER_LIMIT)
