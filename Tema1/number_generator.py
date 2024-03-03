import math
import random

pi = math.pi

low_limit = -pi / 2
high_limit = pi / 2

number_count = 10000


def generate_random():
    return random.uniform(low_limit, high_limit)


def generate_all():
    random_numbers = []

    for _ in range(number_count):
        random_numbers.append(generate_random())

    return random_numbers
