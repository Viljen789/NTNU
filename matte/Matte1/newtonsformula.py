# Define g(x) for fixed-point iteration
import math
def g(x):
    return 4 + 1/7 * math.sin(x)

# Define f(x) and f'(x) for Newton's method
def f_newton(x):
    return 4 + 1/7 * math.sin(x) - x

def f_prime_newton(x):
    return 1/7 * math.cos(x) - 1

# Fixed-point iteration
def fixed_point_iteration(x0, iterations=3):
    x_values = [x0]
    for _ in range(iterations):
        x_next = g(x_values[-1])
        x_values.append(x_next)
    return [round(x, 5) for x in x_values[1:]]

# Newton's method iteration
def newtons_method_iterations(x0, iterations=3):
    x_values = [x0]
    for _ in range(iterations):
        x_next = x_values[-1] - f_newton(x_values[-1]) / f_prime_newton(x_values[-1])
        x_values.append(x_next)
    return [round(x, 5) for x in x_values[1:]]

# Initial guess x0 = 0.39
x0 = 0.39
fixed_point_results = fixed_point_iteration(x0)
newton_results = newtons_method_iterations(x0)

print(fixed_point_results, newton_results)


def printAgeDiff(table):
    for i in range(len(table)-1):
        from datetime import datetime
def current_date():
    yyyy = int(datetime.today().strftime('%Y'))
    mm = int(datetime.today().strftime('%m'))
    dd = int(datetime.today().strftime('%d'))
    return yyyy,mm,dd
# Define g(x) for fixed-point iteration
import math
def g(x):
    return 4 + 1/7 * math.sin(x)

# Define f(x) and f'(x) for Newton's method
def f_newton(x):
    return 4 + 1/7 * math.sin(x) - x

def f_prime_newton(x):
    return 1/7 * math.cos(x) - 1

# Fixed-point iteration
def fixed_point_iteration(x0, iterations=3):
    x_values = [x0]
    for _ in range(iterations):
        x_next = g(x_values[-1])
        x_values.append(x_next)
    return [round(x, 5) for x in x_values[1:]]

# Newton's method iteration
def newtons_method_iterations(x0, iterations=3):
    x_values = [x0]
    for _ in range(iterations):
        x_next = x_values[-1] - f_newton(x_values[-1]) / f_prime_newton(x_values[-1])
        x_values.append(x_next)
    return [round(x, 5) for x in x_values[1:]]

# Initial guess x0 = 0.39
x0 = 0.39
fixed_point_results = fixed_point_iteration(x0)
newton_results = newtons_method_iterations(x0)

print(fixed_point_results, newton_results)


def printAgeDiff(table):
    for i in range(len(table)-1):
        from datetime import datetime
def current_date():
    yyyy = int(datetime.today().strftime('%Y'))
    mm = int(datetime.today().strftime('%m'))
    dd = int(datetime.today().strftime('%d'))
    return yyyy,mm,dd