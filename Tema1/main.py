import sys
import numpy as np

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
    x=1.0
    y=u/10
    z=u/10
    asociativa = True

    if((x+y)+z != x+(y+z)):
        asociativa = False

    print(f"asociativa: {asociativa}")

exercitiu_2()