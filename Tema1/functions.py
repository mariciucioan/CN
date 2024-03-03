import math


def T4(a):
    return (105 * a - 10 * a ** 3) / (105 - 45 * a ** 2 + a ** 4)


def T5(a):
    return (945 * a - 105 * a ** 3 + a ** 5) / (945 - 420 * a ** 2 + 15 * a ** 4)


def T6(a):
    return (10395 * a - 1260 * a ** 3 + 21 * a ** 5) / (10395 - 4275 * a ** 2 + 210 * a ** 4 - a ** 6)


def T7(a):
    return (135135 * a - 17325 * a ** 3 + 378 * a ** 5 - a ** 7) / (
                135135 - 62370 * a ** 2 + 3150 * a ** 4 - 28 * a ** 6)


def T8(a):
    return (2027025 * a - 270270 * a ** 3 + 6930 * a ** 5 - 36 * a ** 7) / (
                2027025 - 945945 * a ** 2 + 51975 * a ** 4 - 530 * a ** 6 + a ** 8)


def T9(a):
    return (34459425 * a - 4729725 * a ** 3 + 135135 * a ** 5 - 990 * a ** 7 + a ** 9) / (
                34459425 - 16216200 * a ** 2 + 945945 * a ** 4 - 13860 * a ** 6 + 45 * a ** 8)


def T(i, a):
    if i == 4:
        return T4(a)
    elif i == 5:
        return T5(a)
    elif i == 6:
        return T6(a)
    elif i == 7:
        return T7(a)
    elif i == 8:
        return T8(a)
    elif i == 9:
        return T9(a)


def S(n, a):
    return T(n, a) / math.sqrt(1 + T(n, a) ** 2)


def C(n, a):
    return 1 / math.sqrt((1 + T(n, a) ** 2))
