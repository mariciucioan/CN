import sys
import numpy as np
from number_generator import generate_all
from functions import T
import math


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
        
exercitiu_3()


    


    