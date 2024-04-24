import numpy as np

# function definition
def F(x, y):
    return 3*x**2 - 12*x + 2*y**2 + 16*y - 10

def calculate_analytical_gradient(x, y):
    partial_x = 2 * x - 2
    partial_y = 2 * y - 2
    return np.array([partial_x, partial_y])

def calculate_approximate_gradient(x, y):
    h = 1e-5
    partial_x = (3*F(x, y) -4*F(x - h, y) + F(x - 2*h, y)) / (2 * h)
    partial_y = (3*F(x, y) -4* F(x, y - h) + F(x, y - 2*h)) / (2 * h)
    return np.array([partial_x, partial_y])

def gradient_descent(start_point, learning_rate_method, gradient_method, max_iterations=1000, epsilon=1e-6):
    x, y = start_point
    iteration = 0
    while True:
        gradient = gradient_method(x, y)
        learning_rate = learning_rate_method(x, y, gradient)
        x_new = x - learning_rate * gradient[0]
        y_new = y - learning_rate * gradient[1]
        if np.linalg.norm(np.array([x_new, y_new]) - np.array([x, y])) < epsilon or iteration >= max_iterations:
            break
        x, y = x_new, y_new
        iteration += 1
    return np.array([x, y]), iteration

def constant_learning_rate(x, y, gradient):
    return 0.01 

def backtracking_learning_rate(x, y, gradient):
    beta = 0.8  # Reduction factor of the learning rate
    eta = 1.0  # Initial learning rate
    p = 1
    h = 1e-5
    while F(x - eta * gradient[0], y - eta * gradient[1]) > F(x, y) - eta**2 * np.linalg.norm(gradient)**2 and p < 8:
        eta *= beta
        p += 1
    return eta

start_point = [5, 5] 
learning_rate_methods = [constant_learning_rate, backtracking_learning_rate]
gradient_methods = [calculate_analytical_gradient, calculate_approximate_gradient]
for grad_method in gradient_methods:
    for learn_method in learning_rate_methods:
        result, iterations = gradient_descent(start_point, learn_method, grad_method)
        print(f"Gradient method: {'Analytical' if grad_method == calculate_analytical_gradient else 'Approximate'}")
        print(f"Learning rate method: {'Constant' if learn_method == constant_learning_rate else 'Backtracking search'}")
        print("Minimum point:", result)
        print("Number of iterations:", iterations)
        print("--------------------")
