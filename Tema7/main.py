import math
import random

def evaluate_polynomial(coefficients, x):
    result = coefficients[0]
    for coef in coefficients[1:]:
        result = result * x + coef
    return result

def horner_form(polynomial):
    n = len(polynomial)
    b = [0] * n
    b[-1] = polynomial[-1]
    for i in range(n - 2, -1, -1):
        b[i] = polynomial[i] + b[i + 1]
    return b

def calculate_delta_x(a, b, c):
    discriminant = math.sqrt(b ** 2 - 4 * a * c)
    if b >= 0:
        return -(2 * c) / (b + discriminant)
    else:
        return -(2 * c) / (b - discriminant)

def muller(coefficients, epsilon, k_max):
    roots = []
    for i in range(0, k_max):
        root = muller_method(coefficients, epsilon)
        if root in roots:
            continue;

        roots.append(root)

    roots = list(set([round(root, 1) for root in roots]))
    return roots

def muller_method(coefficients, epsilon):
    k = 3
    A = max(abs(coef) for coef in coefficients)
    R = (abs(coefficients[0]) + A)/abs(coefficients[0])
    x_values = [random.uniform(-R, R) for _ in range(k)]

    while True:
        h0 = x_values[-2] - x_values[-3]
        h1 = x_values[-1] - x_values[-2]
        if h1 == 0:
            delta_1 = 0
        else:
            delta_1 = (evaluate_polynomial(coefficients, x_values[-1]) - evaluate_polynomial(coefficients, x_values[-2])) / h1
        delta_0 = (evaluate_polynomial(coefficients, x_values[-2]) - evaluate_polynomial(coefficients, x_values[-3])) / h0
        a = (delta_1 - delta_0) / (h1 + h0)
        if a == 0:
            return x_values[-1]

        b = a * h1 + delta_1
        c = evaluate_polynomial(coefficients, x_values[-1])

        discriminant = b ** 2 - 4 * a * c

        if discriminant < 0:
            x_values = [random.uniform(-R, R) for _ in range(3)]
            continue

        sqrt_discriminant = math.sqrt(discriminant)
        root1 = (-b + sqrt_discriminant) / (2 * a)
        root2 = (-b - sqrt_discriminant) / (2 * a)

        if abs(max(root1, root2) - min(root1, root2)) < epsilon:
            print("Converge; STOP.")
            break

        delta_x1 = calculate_delta_x(a, b, c)
        delta_x2 = -2 * c / (b + math.copysign(sqrt_discriminant, b))
        x_new = x_values[-1] + delta_x1 if abs(delta_x1) < abs(delta_x2) else x_values[-1] + delta_x2
        x_values.pop(0)
        x_values.append(x_new)

        if abs(delta_x1) < epsilon or k >= k_max or abs(delta_x1) >= 1e8:
            print("Divergence; STOP.")
            return x_new
            break

    return None

# (x - 1)(x - 2)(x - 3)
coefficients = [1, -6, 11, -6]
epsilon = 1e-13
k_max = 100
roots = muller(coefficients, epsilon, k_max)

with open("roots.txt", "w") as file:
    for root in roots:
        file.write(str(root) + "\n")

print("Roots:", roots)

print(f"P(1)={evaluate_polynomial(coefficients, 1)}")
print(f"P(2)={evaluate_polynomial(coefficients, 2)}")
print(f"P(3)={evaluate_polynomial(coefficients, 3)}")
print(f"P(10)={evaluate_polynomial(coefficients, 10)}")