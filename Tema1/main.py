import math
import sys

import numpy as np

from functions import T, S, C
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

    if (x + y) + z != x + (y + z):
        asociativa = False

    print(f"asociativa: {asociativa}")


def error(exact, calculated):
    return abs(calculated - exact)


exercitiu_2()


def add_in_freq(key, freq_list):
    if key in freq_list:
        freq_list[key] += 1
    else:
        freq_list[key] = 1


def exercitiu_3():
    random_numbers = generate_all()
    freq_tan = {}
    freq_sin = {}
    freq_cos = {}
    for number in random_numbers:
        tan = math.tan(number)
        sin = math.sin(number)
        cos = math.cos(number)

        min_error_tan, min_index_tan = 1000, 4
        min_error_sin, min_index_sin = 1000, 4
        min_error_cos, min_index_cos = 1000, 4

        for i in range(4, 10):
            actual_error_tan = error(T(i, number), tan)
            actual_error_sin = error(S(i, number), sin)
            actual_error_cos = error(C(i, number), cos)

            if actual_error_tan < min_error_tan:
                min_error_tan = actual_error_tan
                min_index_tan = i

            if actual_error_sin < min_error_sin:
                min_error_sin = actual_error_sin
                min_index_sin = i

            if actual_error_cos < min_error_cos:
                min_error_cos = actual_error_cos
                min_index_cos = i

        add_in_freq(min_index_tan, freq_tan)
        add_in_freq(min_index_sin, freq_sin)
        add_in_freq(min_index_cos, freq_cos)

    print(freq_tan)
    print(freq_sin)
    print(freq_cos)

    return freq_tan, freq_sin, freq_cos


def create_combined_plot(freq_lists, function_names):
    plt.figure(figsize=(10, 6))

    colors = ['b', 'g', 'r']  # Colors for different functions

    for i, freq_list in enumerate(freq_lists):
        plt.bar([x + i * 0.25 for x in freq_list.keys()], list(freq_list.values()), width=0.25, color=colors[i],
                label=function_names[i])

    plt.xlabel('T function index')
    plt.ylabel('Min error count')
    plt.title("Frequency of Trigonometric Function Approximations")

    plt.text(0.5, 1.08, f"Generated numbers = {number_count}", transform=plt.gca().transAxes, ha='center')

    for i, freq_list in enumerate(freq_lists):
        for key, value in freq_list.items():
            plt.text(key + i * 0.25, value, str(value), ha='center', va='bottom')

    plt.legend()
    plt.show()


frequency_tan, frequency_sin, frequency_cos = exercitiu_3()
fct_names = ["tan", "sin", "cos"]

create_combined_plot([frequency_tan, frequency_sin, frequency_cos], fct_names)
