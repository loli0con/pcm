import math
import random


def is_prime(num: int):
    if num == 2 or num == 3:
        return True
    if num % 6 != 1 and num % 6 != 5:
        return False
    for i in range(5, int(math.sqrt(num)) + 1, 6):
        if num % i == 0 or num % (i + 2) == 0:
            return False
    return True


def random_number():
    return random.randint(2_000_000_000, 10_000_000_000)
