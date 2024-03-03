import math
import sys

import numpy as np

from functions import T
from number_generator import generate_all, number_count

import matplotlib.pyplot as plt


def exercitiu_1():
    mantissa = sys.float_info.mant_dig
    digits = np.log10(2 ** mantissa)
    m = int(np.floor(digits))
    u = 10 ** (-m)

    print(f"m: {m}\n"
          f"u: {u}\n"
          f"1 + {u} != 1: {1 + u != 1}")

    return u


u = exercitiu_1()


def exercitiu_2():
    x = 1.0
    y = u / 10
    z = u / 10
    asociativa = True

    if ((x + y) + z != x + (y + z)):
        asociativa = False

    print(f"asociativa: {asociativa}")

def error (exact, calculated):
    return abs(calculated - exact)


exercitiu_2()


def exercitiu_3():
    random_numbers = generate_all()
    freq = {}
    for number in random_numbers:
        tan = math.tan(number)
        min_error, min_index = 1000, 4
        for i in range(4,10):
            actual_error = error(T(i, number), tan)
            if ( actual_error < min_error):
                min_error = actual_error
                min_index = i
        if min_index in freq:
            freq[min_index] += 1
        else:
            freq[min_index] = 1
    print(freq)
    return freq

frequency = exercitiu_3()

plt.bar(list(frequency.keys()), list(frequency.values()))

# Add labels and title
plt.xlabel('T function index')
plt.ylabel('Min error count')
plt.title('Frequency of tan approximation')

# Adding values on top of bars
for key, value in frequency.items():
    plt.text(key, value, str(value), ha='center', va='bottom')

plt.text(0.5, 1.1, f"Generated numbers = {number_count}", transform=plt.gca().transAxes, ha='center')

# Show plot
plt.show()