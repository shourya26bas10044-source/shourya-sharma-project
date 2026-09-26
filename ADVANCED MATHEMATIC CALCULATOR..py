# ================================================================
#        ADVANCED MATHEMATICS CALCULATOR
#        WITHOUT USING ANY LIBRARY OR MODULE
# ================================================================

"""
INTRODUCTION
------------
This is an Advanced Mathematics Calculator developed completely
using basic Python.

NO external library or module is used.

The calculator can perform:
1. Arithmetic operations
2. Scientific calculations
3. Trigonometric functions
4. Inverse trigonometric functions
5. Logarithmic and exponential functions
6. Polynomial calculations and roots
7. Function roots using Newton-Raphson method
8. Complex number calculations
9. Statistics
10. Matrix operations and determinant
11. Unit conversion
12. Number-system conversion
13. Degree and radian conversion
14. Factorial, square root, absolute value and length

The mathematical functions such as sin, cos, tan, log, sqrt,
exp etc. are calculated using mathematical algorithms instead
of importing Python libraries.

Project principle:
    INPUT -> PROCESS -> OUTPUT

Author: Student Mathematics Project
"""

# ================================================================
# CONSTANTS
# ================================================================

PI = 3.141592653589793
E = 2.718281828459045

EPS = 0.000000000001
MAX_ITER = 100


# ================================================================
# BASIC MATHEMATICAL FUNCTIONS
# ================================================================

def absolute(x):
    if x < 0:
        return -x
    return x


def power(x, n):
    """
    Calculates x^n without using pow().
    Works for integer powers.
    """
    if n == 0:
        return 1

    negative = False

    if n < 0:
        negative = True
        n = -n

    result = 1

    for i in range(n):
        result *= x

    if negative:
        return 1 / result

    return result


def factorial(n):
    if n < 0 or int(n) != n:
        return None

    result = 1

    for i in range(1, int(n) + 1):
        result *= i

    return result


# ================================================================
# SQUARE ROOT USING NEWTON-RAPHSON
# ================================================================

def square_root(x):
    if x < 0:
        return None

    if x == 0:
        return 0

    guess = x

    for i in range(100):
        new_guess = (guess + x / guess) / 2

        if absolute(new_guess - guess) < EPS:
            break

        guess = new_guess

    return new_guess


# ================================================================
# EXPONENTIAL FUNCTION
# e^x USING TAYLOR SERIES
# ================================================================

def exponential(x):

    # Reduce large negative/positive values
    if x < -50:
        return 0

    if x > 50:
        return 51847055285870724608

    result = 1
    term = 1

    for n in range(1, 100):
        term = term * x / n
        result += term

        if absolute(term) < EPS:
            break

    return result


# ================================================================
# NATURAL LOGARITHM
# ================================================================

def ln(x):

    if x <= 0:
        return None

    # Transformation:
    # ln(x) = 2[z + z^3/3 + z^5/5 + ...]
    # where z = (x-1)/(x+1)

    z = (x - 1) / (x + 1)

    result = 0
    power_z = z

    for n in range(1, 10000, 2):

        term = power_z / n
        result += term

        if absolute(term) < EPS:
            break

        power_z *= z * z

    return 2 * result


def log10(x):

    if x <= 0:
        return None

    return ln(x) / ln(10)


# ================================================================
# DEGREE <-> RADIAN
# ================================================================

def degree_to_radian(degree):
    return degree * PI / 180


def radian_to_degree(radian):
    return radian * 180 / PI


# ================================================================
# ANGLE NORMALIZATION
# ================================================================

def normalize_angle(x):

    two_pi = 2 * PI

    while x > PI:
        x -= two_pi

    while x < -PI:
        x += two_pi

    return x


# ================================================================
# SIN USING TAYLOR SERIES
# ================================================================

def sine(x):

    x = normalize_angle(x)

    result = 0
    term = x

    for n in range(1, 50):

        result += term

        term = -term * x * x / ((2 * n) * (2 * n + 1))

        if absolute(term) < EPS:
            break

    return result


# ================================================================
# COS USING TAYLOR SERIES
# ================================================================

def cosine(x):

    x = normalize_angle(x)

    result = 0
    term = 1

    for n in range(1, 50):

        result += term

        term = -term * x * x / ((2 * n - 1) * (2 * n))

        if absolute(term) < EPS:
            break

    return result


# ================================================================
# TAN
# ================================================================

def tangent(x):

    c = cosine(x)

    if absolute(c) < EPS:
        return None

    return sine(x) / c


# ================================================================
# ARCTAN USING NEWTON METHOD
# ================================================================

def arctan(x):

    if x > 1:
        return PI / 2 - arctan(1 / x)

    if x < -1:
        return -PI / 2 - arctan(1 / x)

    result = 0

    # Taylor series:
    # atan(x) = x - x^3/3 + x^5/5 ...

    power_x = x

    for n in range(1, 10000, 2):

        term = power_x / n

        if ((n - 1) // 2) % 2 == 0:
            result += term
        else:
            result -= term

        if absolute(term) < EPS:
            break

        power_x *= x * x

    return result


# ================================================================
# ARCSIN
# ================================================================

def arcsin(x):

    if x < -1 or x > 1:
        return None

    if x == 1:
        return PI / 2

    if x == -1:
        return -PI / 2

    # asin(x) = atan(x / sqrt(1-x²))

    denominator = square_root(1 - x * x)

    if denominator == 0:
        return PI / 2

    return arctan(x / denominator)


# ================================================================
# ARCCOS
# ================================================================

def arccos(x):

    if x < -1 or x > 1:
        return None

    return PI / 2 - arcsin(x)


# ================================================================
# NUMBER ROUNDING
# ================================================================

def clean(x):

    if isinstance(x, float):

        if absolute(x) < EPS:
            return 0

        rounded = round(x, 10)

        if rounded == int(rounded):
            return int(rounded)

        return rounded

    return x


# ================================================================
# POLYNOMIAL FUNCTIONS
# ================================================================

def polynomial_degree(coefficients):

    degree = len(coefficients) - 1

    while degree > 0 and coefficients[0] == 0:

        coefficients = coefficients[1:]
        degree -= 1

    return degree


def polynomial_value(coefficients, x):

    """
    Horner's method

    Example:
    2x² + 3x + 4

    coefficients = [2, 3, 4]
    """

    result = 0

    for coefficient in coefficients:

        result = result * x + coefficient

    return result


def polynomial_derivative(coefficients):

    degree = len(coefficients) - 1

    derivative = []

    for i in range(degree):

        derivative.append(
            coefficients[i] * (degree - i)
        )

    return derivative


# ================================================================
# POLYNOMIAL ROOTS
# ================================================================

def polynomial_roots(coefficients):

    degree = polynomial_degree(coefficients)

    # Remove leading zeros
    while len(coefficients) > 1 and coefficients[0] == 0:
        coefficients = coefficients[1:]

    degree = len(coefficients) - 1

    # ------------------------------------------------------------
    # LINEAR
    # ax + b = 0
    # ------------------------------------------------------------

    if degree == 1:

        a = coefficients[0]
        b = coefficients[1]

        if a == 0:
            return []

        return [-b / a]

    # ------------------------------------------------------------
    # QUADRATIC
    # ax² + bx + c = 0
    # ------------------------------------------------------------

    if degree == 2:

        a = coefficients[0]
        b = coefficients[1]
        c = coefficients[2]

        discriminant = b * b - 4 * a * c

        if discriminant >= 0:

            root1 = (-b + square_root(discriminant)) / (2 * a)
            root2 = (-b - square_root(discriminant)) / (2 * a)

            return [root1, root2]

        else:

            real = -b / (2 * a)
            imaginary = square_root(-discriminant) / (2 * a)

            return [
                (real, imaginary),
                (real, -imaginary)
            ]

    # ------------------------------------------------------------
    # HIGHER DEGREE
    # NUMERICAL SEARCH
    # ------------------------------------------------------------

    roots = []

    # Search for roots between -100 and 100
    step = 0.5

    x = -100

    previous_x = x
    previous_y = polynomial_value(coefficients, x)

    while x <= 100:

        y = polynomial_value(coefficients, x)

        if previous_y * y < 0:

            left = previous_x
            right = x

            for i in range(100):

                middle = (left + right) / 2
                middle_y = polynomial_value(coefficients, middle)

                if absolute(middle_y) < EPS:
                    break

                if previous_y * middle_y < 0:

                    right = middle

                else:

                    left = middle
                    previous_y = middle_y

            root = (left + right) / 2

            duplicate = False

            for r in roots:

                if absolute(r - root) < 0.0001:
                    duplicate = True

            if not duplicate:
                roots.append(root)

        previous_x = x
        previous_y = y

        x += step

    return roots


# ================================================================
# FUNCTION ROOT USING NEWTON-RAPHSON
# ================================================================

def function_root(coefficients, initial_guess):

    derivative = polynomial_derivative(coefficients)

    x = initial_guess

    for i in range(MAX_ITER):

        fx = polynomial_value(coefficients, x)
        fdx = polynomial_value(derivative, x)

        if absolute(fdx) < EPS:
            return None

        new_x = x - fx / fdx

        if absolute(new_x - x) < EPS:
            return new_x

        x = new_x

    return x


# ================================================================
# COMPLEX NUMBERS
# ================================================================

def complex_add(a, b):

    return (a[0] + b[0], a[1] + b[1])


def complex_subtract(a, b):

    return (a[0] - b[0], a[1] - b[1])


def complex_multiply(a, b):

    real = a[0] * b[0] - a[1] * b[1]
    imaginary = a[0] * b[1] + a[1] * b[0]

    return (real, imaginary)


def complex_divide(a, b):

    denominator = b[0] * b[0] + b[1] * b[1]

    if denominator == 0:
        return None

    real = (a[0] * b[0] + a[1] * b[1]) / denominator

    imaginary = (a[1] * b[0] - a[0] * b[1]) / denominator

    return (real, imaginary)


def complex_modulus(a):

    return square_root(a[0] * a[0] + a[1] * a[1])


def complex_conjugate(a):

    return (a[0], -a[1])


def print_complex(z):

    real = clean(z[0])
    imaginary = clean(z[1])

    if imaginary >= 0:
        print(real, "+", imaginary, "i")
    else:
        print(real, "-", absolute(imaginary), "i")


# ================================================================
# STATISTICS
# ================================================================

def mean(data):

    if len(data) == 0:
        return None

    total = 0

    for x in data:
        total += x

    return total / len(data)


def median(data):

    if len(data) == 0:
        return None

    values = data[:]

    # Bubble sort
    for i in range(len(values)):

        for j in range(len(values) - i - 1):

            if values[j] > values[j + 1]:

                values[j], values[j + 1] = values[j + 1], values[j]

    n = len(values)

    if n % 2 == 1:

        return values[n // 2]

    else:

        return (values[n // 2 - 1] + values[n // 2]) / 2


def mode(data):

    if len(data) == 0:
        return None

    highest_count = 0
    modes = []

    for x in data:

        count = 0

        for y in data:

            if x == y:
                count += 1

        if count > highest_count:

            highest_count = count
            modes = [x]

        elif count == highest_count and x not in modes:

            modes.append(x)

    if highest_count == 1:
        return "No mode"

    return modes


def variance(data):

    m = mean(data)

    total = 0

    for x in data:

        total += (x - m) * (x - m)

    return total / len(data)


def standard_deviation(data):

    return square_root(variance(data))


# ================================================================
# MATRIX FUNCTIONS
# ================================================================

def matrix_input(rows, columns):

    matrix = []

    print("Enter matrix row by row:")

    for i in range(rows):

        row = []

        for j in range(columns):

            value = float(input(
                "Element [" + str(i + 1) + "][" + str(j + 1) + "]: "
            ))

            row.append(value)

        matrix.append(row)

    return matrix


def print_matrix(matrix):

    for row in matrix:

        for value in row:

            print(str(clean(value)).rjust(10), end=" ")

        print()


def matrix_add(A, B):

    rows = len(A)
    columns = len(A[0])

    result = []

    for i in range(rows):

        row = []

        for j in range(columns):

            row.append(A[i][j] + B[i][j])

        result.append(row)

    return result


def matrix_subtract(A, B):

    rows = len(A)
    columns = len(A[0])

    result = []

    for i in range(rows):

        row = []

        for j in range(columns):

            row.append(A[i][j] - B[i][j])

        result.append(row)

    return result


def matrix_multiply(A, B):

    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])

    if cols_A != rows_B:
        return None

    result = []

    for i in range(rows_A):

        row = []

        for j in range(cols_B):

            total = 0

            for k in range(cols_A):

                total += A[i][k] * B[k][j]

            row.append(total)

        result.append(row)

    return result


def transpose(A):

    rows = len(A)
    columns = len(A[0])

    result = []

    for j in range(columns):

        row = []

        for i in range(rows):

            row.append(A[i][j])

        result.append(row)

    return result


# ================================================================
# MATRIX DETERMINANT
# ================================================================

def determinant(A):

    n = len(A)

    if n == 1:
        return A[0][0]

    if n == 2:

        return A[0][0] * A[1][1] - A[0][1] * A[1][0]

    result = 0

    for column in range(n):

        minor = []

        for i in range(1, n):

            row = []

            for j in range(n):

                if j != column:
                    row.append(A[i][j])

            minor.append(row)

        sign = 1

        if column % 2 == 1:
            sign = -1

        result += sign * A[0][column] * determinant(minor)

    return result


# ================================================================
# MATRIX INVERSE
# ================================================================

def matrix_inverse(A):

    n = len(A)

    det = determinant(A)

    if absolute(det) < EPS:
        return None

    # Create augmented matrix [A | I]

    augmented = []

    for i in range(n):

        row = []

        for j in range(n):
            row.append(A[i][j])

        for j in range(n):

            if i == j:
                row.append(1)

            else:
                row.append(0)

        augmented.append(row)

    # Gauss-Jordan elimination

    for i in range(n):

        pivot = augmented[i][i]

        if absolute(pivot) < EPS:

            for k in range(i + 1, n):

                if absolute(augmented[k][i]) > EPS:

                    augmented[i], augmented[k] = (
                        augmented[k],
                        augmented[i]
                    )

                    pivot = augmented[i][i]

                    break

        if absolute(pivot) < EPS:
            return None

        # Divide row by pivot

        for j in range(2 * n):

            augmented[i][j] /= pivot

        # Make other elements zero

        for k in range(n):

            if k != i:

                factor = augmented[k][i]

                for j in range(2 * n):

                    augmented[k][j] -= factor * augmented[i][j]

    inverse = []

    for i in range(n):

        inverse.append(augmented[i][n:])

    return inverse


# ================================================================
# NUMBER SYSTEM CONVERSION
# ================================================================

digits = "0123456789ABCDEF"


def decimal_to_base(number, base):

    if number == 0:
        return "0"

    negative = False

    if number < 0:

        negative = True
        number = -number

    result = ""

    while number > 0:

        remainder = number % base

        result = digits[remainder] + result

        number = number // base

    if negative:
        result = "-" + result

    return result


def base_to_decimal(number, base):

    number = number.upper()

    negative = False

    if number[0] == "-":

        negative = True
        number = number[1:]

    result = 0

    for character in number:

        value = digits.index(character)

        if value >= base:
            return None

        result = result * base + value

    if negative:
        result = -result

    return result


def number_conversion():

    print("\nNUMBER SYSTEM CONVERSION")
    print("------------------------")
    print("1. Binary")
    print("2. Octal")
    print("3. Decimal")
    print("4. Hexadecimal")

    choice = input("Select input number system: ")

    systems = {
        "1": 2,
        "2": 8,
        "3": 10,
        "4": 16
    }

    if choice not in systems:

        print("Invalid choice.")
        return

    base = systems[choice]

    number = input("Enter number: ")

    decimal = base_to_decimal(number, base)

    if decimal is None:

        print("Invalid number for selected base.")
        return

    print("\nConversions:")

    print("Binary      :", decimal_to_base(decimal, 2))
    print("Octal       :", decimal_to_base(decimal, 8))
    print("Decimal     :", decimal)
    print("Hexadecimal :", decimal_to_base(decimal, 16))


# ================================================================
# UNIT CONVERSION
# ================================================================

def unit_conversion():

    print("\nUNIT CONVERSION")
    print("----------------")

    print("1. Length")
    print("2. Mass")
    print("3. Temperature")
    print("4. Time")
    print("5. Speed")
    print("6. Area")
    print("7. Volume")

    choice = input("Select category: ")

    value = float(input("Enter value: "))

    # ------------------------------------------------------------
    # LENGTH
    # ------------------------------------------------------------

    if choice == "1":

        print("\nLength units:")
        print("1. meter")
        print("2. kilometer")
        print("3. centimeter")
        print("4. millimeter")
        print("5. mile")
        print("6. foot")
        print("7. inch")

        unit = input("Select unit: ")

        # Convert everything to meters

        factors = {
            "1": 1,
            "2": 1000,
            "3": 0.01,
            "4": 0.001,
            "5": 1609.344,
            "6": 0.3048,
            "7": 0.0254
        }

        names = {
            "1": "meter",
            "2": "kilometer",
            "3": "centimeter",
            "4": "millimeter",
            "5": "mile",
            "6": "foot",
            "7": "inch"
        }

        if unit not in factors:

            print("Invalid unit.")
            return

        meters = value * factors[unit]

        print("\nConversions:")

        for key in factors:

            result = meters / factors[key]

            print(
                names[key],
                "=",
                clean(result)
            )

    # ------------------------------------------------------------
    # MASS
    # ------------------------------------------------------------

    elif choice == "2":

        print("\nMass units:")
        print("1. kilogram")
        print("2. gram")
        print("3. milligram")
        print("4. pound")

        unit = input("Select unit: ")

        factors = {
            "1": 1,
            "2": 0.001,
            "3": 0.000001,
            "4": 0.45359237
        }

        names = {
            "1": "kg",
            "2": "g",
            "3": "mg",
            "4": "pound"
        }

        if unit not in factors:

            print("Invalid unit.")
            return

        kg = value * factors[unit]

        for key in factors:

            print(
                names[key],
                "=",
                clean(kg / factors[key])
            )

    # ------------------------------------------------------------
    # TEMPERATURE
    # ------------------------------------------------------------

    elif choice == "3":

        print("\nTemperature:")
        print("1. Celsius")
        print("2. Fahrenheit")
        print("3. Kelvin")

        unit = input("Select unit: ")

        if unit == "1":

            c = value

        elif unit == "2":

            c = (value - 32) * 5 / 9

        elif unit == "3":

            c = value - 273.15

        else:

            print("Invalid unit.")
            return

        print("Celsius    :", clean(c))
        print("Fahrenheit :", clean(c * 9 / 5 + 32))
        print("Kelvin     :", clean(c + 273.15))

    # ------------------------------------------------------------
    # TIME
    # ------------------------------------------------------------

    elif choice == "4":

        print("\nTime units:")
        print("1. seconds")
        print("2. minutes")
        print("3. hours")
        print("4. days")

        unit = input("Select unit: ")

        factors = {
            "1": 1,
            "2": 60,
            "3": 3600,
            "4": 86400
        }

        names = {
            "1": "seconds",
            "2": "minutes",
            "3": "hours",
            "4": "days"
        }

        if unit not in factors:

            print("Invalid unit.")
            return

        seconds = value * factors[unit]

        for key in factors:

            print(
                names[key],
                "=",
                clean(seconds / factors[key])
            )

    # ------------------------------------------------------------
    # SPEED
    # ------------------------------------------------------------

    elif choice == "5":

        print("\nSpeed:")
        print("1. m/s")
        print("2. km/h")
        print("3. mph")

        unit = input("Select unit: ")

        if unit == "1":

            ms = value

        elif unit == "2":

            ms = value / 3.6

        elif unit == "3":

            ms = value * 0.44704

        else:

            print("Invalid unit.")
            return

        print("m/s  :", clean(ms))
        print("km/h :", clean(ms * 3.6))
        print("mph  :", clean(ms / 0.44704))

    # ------------------------------------------------------------
    # AREA
    # ------------------------------------------------------------

    elif choice == "6":

        print("\nArea:")
        print("1. m²")
        print("2. km²")
        print("3. cm²")
        print("4. acre")

        unit = input("Select unit: ")

        factors = {
            "1": 1,
            "2": 1000000,
            "3": 0.0001,
            "4": 4046.8564224
        }

        names = {
            "1": "m²",
            "2": "km²",
            "3": "cm²",
            "4": "acre"
        }

        if unit not in factors:

            print("Invalid unit.")
            return

        square_meter = value * factors[unit]

        for key in factors:

            print(
                names[key],
                "=",
                clean(square_meter / factors[key])
            )

    # ------------------------------------------------------------
    # VOLUME
    # ------------------------------------------------------------

    elif choice == "7":

        print("\nVolume:")
        print("1. liter")
        print("2. milliliter")
        print("3. cubic meter")
        print("4. gallon")

        unit = input("Select unit: ")

        factors = {
            "1": 1,
            "2": 0.001,
            "3": 1000,
            "4": 3.785411784
        }

        names = {
            "1": "liter",
            "2": "milliliter",
            "3": "m³",
            "4": "gallon"
        }

        if unit not in factors:

            print("Invalid unit.")
            return

        liters = value * factors[unit]

        for key in factors:

            print(
                names[key],
                "=",
                clean(liters / factors[key])
            )

    else:

        print("Invalid category.")


# ================================================================
# ARITHMETIC CALCULATOR
# ================================================================

def arithmetic_calculator():

    print("\nARITHMETIC CALCULATOR")
    print("---------------------")

    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Integer Division")
    print("7. Power")

    choice = input("Select operation: ")

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if choice == "1":
        result = a + b

    elif choice == "2":
        result = a - b

    elif choice == "3":
        result = a * b

    elif choice == "4":

        if b == 0:

            print("Cannot divide by zero.")
            return

        result = a / b

    elif choice == "5":

        result = a % b

    elif choice == "6":

        result = a // b

    elif choice == "7":

        if int(b) == b:
            result = power(a, int(b))
        else:
            result = exponential(b * ln(a))

    else:

        print("Invalid operation.")
        return

    print("Result =", clean(result))


# ================================================================
# SCIENTIFIC CALCULATOR
# ================================================================

def scientific_calculator():

    print("\nSCIENTIFIC CALCULATOR")
    print("---------------------")

    print("1. Square Root")
    print("2. Square")
    print("3. Cube")
    print("4. Factorial")
    print("5. Absolute Value")
    print("6. Exponential e^x")
    print("7. Natural Log ln(x)")
    print("8. Log10(x)")
    print("9. π")
    print("10. e")

    choice = input("Select operation: ")

    if choice == "1":

        x = float(input("Enter x: "))
        result = square_root(x)

        if result is None:
            print("Square root of negative number is not real.")
            return

    elif choice == "2":

        x = float(input("Enter x: "))
        result = x * x

    elif choice == "3":

        x = float(input("Enter x: "))
        result = x * x * x

    elif choice == "4":

        x = int(input("Enter positive integer: "))
        result = factorial(x)

        if result is None:
            print("Invalid factorial.")
            return

    elif choice == "5":

        x = float(input("Enter x: "))
        result = absolute(x)

    elif choice == "6":

        x = float(input("Enter x: "))
        result = exponential(x)

    elif choice == "7":

        x = float(input("Enter x: "))
        result = ln(x)

        if result is None:
            print("Logarithm requires x > 0.")
            return

    elif choice == "8":

        x = float(input("Enter x: "))
        result = log10(x)

        if result is None:
            print("Logarithm requires x > 0.")
            return

    elif choice == "9":

        result = PI

    elif choice == "10":

        result = E

    else:

        print("Invalid choice.")
        return

    print("Result =", clean(result))


# ================================================================
# TRIGONOMETRIC CALCULATOR
# ================================================================

def trigonometry():

    print("\nTRIGONOMETRY")
    print("------------")

    print("1. sin")
    print("2. cos")
    print("3. tan")
    print("4. sin^-1")
    print("5. cos^-1")
    print("6. tan^-1")
    print("7. Degree -> Radian")
    print("8. Radian -> Degree")

    choice = input("Select operation: ")

    x = float(input("Enter value: "))

    if choice == "1":

        angle = degree_to_radian(x)
        result = sine(angle)

        print("sin(", x, "° ) =", clean(result))

    elif choice == "2":

        angle = degree_to_radian(x)
        result = cosine(angle)

        print("cos(", x, "° ) =", clean(result))

    elif choice == "3":

        angle = degree_to_radian(x)
        result = tangent(angle)

        if result is None:

            print("tan is undefined for this angle.")
            return

        print("tan(", x, "° ) =", clean(result))

    elif choice == "4":

        result = arcsin(x)

        if result is None:

            print("Input must be between -1 and 1.")
            return

        print(
            "sin^-1(",
            x,
            ") =",
            clean(radian_to_degree(result)),
            "degrees"
        )

    elif choice == "5":

        result = arccos(x)

        if result is None:

            print("Input must be between -1 and 1.")
            return

        print(
            "cos^-1(",
            x,
            ") =",
            clean(radian_to_degree(result)),
            "degrees"
        )

    elif choice == "6":

        result = arctan(x)

        print(
            "tan^-1(",
            x,
            ") =",
            clean(radian_to_degree(result)),
            "degrees"
        )

    elif choice == "7":

        print(
            x,
            "degrees =",
            clean(degree_to_radian(x)),
            "radians"
        )

    elif choice == "8":

        print(
            x,
            "radians =",
            clean(radian_to_degree(x)),
            "degrees"
        )

    else:

        print("Invalid choice.")


# ================================================================
# POLYNOMIAL MENU
# ================================================================

def polynomial_calculator():

    print("\nPOLYNOMIAL CALCULATOR")
    print("---------------------")

    print("Example:")
    print("2x^3 + 3x^2 - 5x + 7")
    print("Enter coefficients as:")
    print("2 3 -5 7")

    data = input("Enter coefficients: ")

    parts = data.split()

    coefficients = []

    for item in parts:

        coefficients.append(float(item))

    print("\n1. Find degree")
    print("2. Evaluate polynomial")
    print("3. Find roots")
    print("4. Find root using Newton-Raphson")

    choice = input("Select operation: ")

    degree = polynomial_degree(coefficients)

    if choice == "1":

        print("Degree =", degree)

    elif choice == "2":

        x = float(input("Enter x: "))

        result = polynomial_value(coefficients, x)

        print("P(", x, ") =", clean(result))

    elif choice == "3":

        roots = polynomial_roots(coefficients)

        if len(roots) == 0:

            print(
                "No real roots were detected in the numerical search."
            )

        else:

            print("Roots:")

            for root in roots:

                if isinstance(root, tuple):

                    print(
                        clean(root[0]),
                        "+",
                        clean(root[1]),
                        "i"
                    )

                else:

                    print(clean(root))

    elif choice == "4":

        guess = float(input("Enter initial guess: "))

        root = function_root(coefficients, guess)

        if root is None:

            print(
                "Newton-Raphson failed. "
                "Try another initial guess."
            )

        else:

            print("Approximate root =", clean(root))

    else:

        print("Invalid choice.")


# ================================================================
# COMPLEX NUMBER CALCULATOR
# ================================================================

def complex_calculator():

    print("\nCOMPLEX NUMBER CALCULATOR")
    print("-------------------------")

    print("Complex number = a + bi")

    a = float(input("Real part of first number: "))
    b = float(input("Imaginary part of first number: "))

    c = float(input("Real part of second number: "))
    d = float(input("Imaginary part of second number: "))

    z1 = (a, b)
    z2 = (c, d)

    print("\n1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus of first number")
    print("6. Conjugate of first number")

    choice = input("Select operation: ")

    if choice == "1":

        result = complex_add(z1, z2)
        print_complex(result)

    elif choice == "2":

        result = complex_subtract(z1, z2)
        print_complex(result)

    elif choice == "3":

        result = complex_multiply(z1, z2)
        print_complex(result)

    elif choice == "4":

        result = complex_divide(z1, z2)

        if result is None:

            print("Division by zero is not allowed.")

        else:

            print_complex(result)

    elif choice == "5":

        print("Modulus =", clean(complex_modulus(z1)))

    elif choice == "6":

        result = complex_conjugate(z1)
        print_complex(result)

    else:

        print("Invalid choice.")


# ================================================================
# STATISTICS MENU
# ================================================================

def statistics_calculator():

    print("\nSTATISTICS CALCULATOR")
    print("---------------------")

    data_input = input(
        "Enter numbers separated by spaces: "
    )

    parts = data_input.split()

    data = []

    for item in parts:

        data.append(float(item))

    if len(data) == 0:

        print("No data entered.")
        return

    print("\n1. Mean")
    print("2. Median")
    print("3. Mode")
    print("4. Variance")
    print("5. Standard Deviation")
    print("6. Minimum")
    print("7. Maximum")
    print("8. Range")
    print("9. Complete Statistics")

    choice = input("Select operation: ")

    if choice == "1":

        print("Mean =", clean(mean(data)))

    elif choice == "2":

        print("Median =", clean(median(data)))

    elif choice == "3":

        print("Mode =", mode(data))

    elif choice == "4":

        print("Variance =", clean(variance(data)))

    elif choice == "5":

        print(
            "Standard Deviation =",
            clean(standard_deviation(data))
        )

    elif choice == "6":

        minimum = data[0]

        for x in data:

            if x < minimum:
                minimum = x

        print("Minimum =", minimum)

    elif choice == "7":

        maximum = data[0]

        for x in data:

            if x > maximum:
                maximum = x

        print("Maximum =", maximum)

    elif choice == "8":

        minimum = data[0]
        maximum = data[0]

        for x in data:

            if x < minimum:
                minimum = x

            if x > maximum:
                maximum = x

        print("Range =", maximum - minimum)

    elif choice == "9":

        minimum = data[0]
        maximum = data[0]

        for x in data:

            if x < minimum:
                minimum = x

            if x > maximum:
                maximum = x

        print("Count              =", len(data))
        print("Mean               =", clean(mean(data)))
        print("Median             =", clean(median(data)))
        print("Mode               =", mode(data))
        print("Variance           =", clean(variance(data)))
        print(
            "Standard Deviation =",
            clean(standard_deviation(data))
        )
        print("Minimum            =", minimum)
        print("Maximum            =", maximum)
        print("Range              =", maximum - minimum)

    else:

        print("Invalid choice.")


# ================================================================
# MATRIX CALCULATOR
# ================================================================

def matrix_calculator():

    print("\nMATRIX CALCULATOR")
    print("-----------------")

    print("1. Matrix Addition")
    print("2. Matrix Subtraction")
    print("3. Matrix Multiplication")
    print("4. Transpose")
    print("5. Determinant")
    print("6. Inverse")

    choice = input("Select operation: ")

    # ------------------------------------------------------------
    # ADDITION
    # ------------------------------------------------------------

    if choice == "1":

        rows = int(input("Number of rows: "))
        columns = int(input("Number of columns: "))

        print("\nMatrix A")
        A = matrix_input(rows, columns)

        print("\nMatrix B")
        B = matrix_input(rows, columns)

        result = matrix_add(A, B)

        print("\nA + B =")
        print_matrix(result)

    # ------------------------------------------------------------
    # SUBTRACTION
    # ------------------------------------------------------------

    elif choice == "2":

        rows = int(input("Number of rows: "))
        columns = int(input("Number of columns: "))

        print("\nMatrix A")
        A = matrix_input(rows, columns)

        print("\nMatrix B")
        B = matrix_input(rows, columns)

        result = matrix_subtract(A, B)

        print("\nA - B =")
        print_matrix(result)

    # ------------------------------------------------------------
    # MULTIPLICATION
    # ------------------------------------------------------------

    elif choice == "3":

        rows_A = int(input("Rows of A: "))
        cols_A = int(input("Columns of A: "))

        rows_B = int(input("Rows of B: "))
        cols_B = int(input("Columns of B: "))

        if cols_A != rows_B:

            print(
                "Matrix multiplication not possible."
            )

            return

        print("\nMatrix A")
        A = matrix_input(rows_A, cols_A)

        print("\nMatrix B")
        B = matrix_input(rows_B, cols_B)

        result = matrix_multiply(A, B)

        print("\nA × B =")
        print_matrix(result)

    # ------------------------------------------------------------
    # TRANSPOSE
    # ------------------------------------------------------------

    elif choice == "4":

        rows = int(input("Number of rows: "))
        columns = int(input("Number of columns: "))

        A = matrix_input(rows, columns)

        result = transpose(A)

        print("\nTranspose =")
        print_matrix(result)

    # ------------------------------------------------------------
    # DETERMINANT
    # ------------------------------------------------------------

    elif choice == "5":

        n = int(input("Order of square matrix: "))

        A = matrix_input(n, n)

        result = determinant(A)

        print("Determinant =", clean(result))

    # ------------------------------------------------------------
    # INVERSE
    # ------------------------------------------------------------

    elif choice == "6":

        n = int(input("Order of square matrix: "))

        A = matrix_input(n, n)

        result = matrix_inverse(A)

        if result is None:

            print(
                "Matrix has no inverse because "
                "its determinant is zero."
            )

        else:

            print("\nInverse =")
            print_matrix(result)

    else:

        print("Invalid choice.")


# ================================================================
# LENGTH FUNCTION
# ================================================================

def length_calculator():

    print("\nLENGTH CALCULATOR")
    print("-----------------")

    print("1. Length of text")
    print("2. Length of a list")

    choice = input("Select option: ")

    if choice == "1":

        text = input("Enter text: ")

        print("Length =", len(text))

    elif choice == "2":

        data = input(
            "Enter items separated by spaces: "
        )

        values = data.split()

        print("Length =", len(values))

    else:

        print("Invalid choice.")


# ================================================================
# SHAPE CALCULATOR
# NO LIBRARY / NO MODULE
# ================================================================


# ================================================================
# SAFE POSITIVE NUMBER INPUT
# ================================================================

def get_positive_number(message):

    while True:

        try:

            value = float(input(message))

            if value <= 0:

                print(
                    "Invalid input! "
                    "Please enter a number greater than 0."
                )

            else:

                return value

        except ValueError:

            print(
                "Invalid input! "
                "Please enter a numeric value."
            )


# ================================================================
# CIRCLE
# ================================================================

def shape_circle():

    print("\n--- CIRCLE ---")

    r = get_positive_number("Enter radius: ")

    print("\nWhat do you want to calculate?")
    print("1. Area")
    print("2. Circumference")

    choice = input("Enter your choice: ")

    if choice == "1":

        area = PI * r * r

        print("Area =", clean(area))

    elif choice == "2":

        circumference = 2 * PI * r

        print(
            "Circumference =",
            clean(circumference)
        )

    else:

        print("Invalid choice!")


# ================================================================
# SQUARE
# ================================================================

def shape_square():

    print("\n--- SQUARE ---")

    a = get_positive_number("Enter side: ")

    print("\nWhat do you want to calculate?")
    print("1. Area")
    print("2. Perimeter")

    choice = input("Enter your choice: ")

    if choice == "1":

        area = a * a

        print("Area =", clean(area))

    elif choice == "2":

        perimeter = 4 * a

        print(
            "Perimeter =",
            clean(perimeter)
        )

    else:

        print("Invalid choice!")


# ================================================================
# RECTANGLE
# ================================================================

def shape_rectangle():

    print("\n--- RECTANGLE ---")

    length = get_positive_number(
        "Enter length: "
    )

    breadth = get_positive_number(
        "Enter breadth: "
    )

    print("\nWhat do you want to calculate?")
    print("1. Area")
    print("2. Perimeter")

    choice = input("Enter your choice: ")

    if choice == "1":

        area = length * breadth

        print("Area =", clean(area))

    elif choice == "2":

        perimeter = 2 * (length + breadth)

        print(
            "Perimeter =",
            clean(perimeter)
        )

    else:

        print("Invalid choice!")


# ================================================================
# TRIANGLE
# ================================================================

def shape_triangle():

    print("\n--- TRIANGLE ---")

    while True:

        a = get_positive_number(
            "Enter side 1: "
        )

        b = get_positive_number(
            "Enter side 2: "
        )

        c = get_positive_number(
            "Enter side 3: "
        )

        # Triangle inequality theorem

        if (
            a + b > c
            and
            a + c > b
            and
            b + c > a
        ):

            break

        print("\nInvalid triangle!")

        print(
            "The sum of any two sides "
            "must be greater than the third side."
        )

        print("Please enter the sides again.\n")

    print("\nWhat do you want to calculate?")
    print("1. Area")
    print("2. Perimeter")

    choice = input("Enter your choice: ")

    if choice == "1":

        # Heron's formula

        s = (a + b + c) / 2

        value = (
            s *
            (s - a) *
            (s - b) *
            (s - c)
        )

        area = square_root(value)

        if area is None:

            print("Unable to calculate area.")

        else:

            print(
                "Area =",
                clean(area)
            )

    elif choice == "2":

        perimeter = a + b + c

        print(
            "Perimeter =",
            clean(perimeter)
        )

    else:

        print("Invalid choice!")


# ================================================================
# CUBE
# ================================================================

def shape_cube():

    print("\n--- CUBE ---")

    a = get_positive_number(
        "Enter side: "
    )

    print("\nWhat do you want to calculate?")
    print("1. Volume")
    print("2. TSA")
    print("3. CSA")

    choice = input("Enter your choice: ")

    if choice == "1":

        volume = a * a * a

        print(
            "Volume =",
            clean(volume)
        )

    elif choice == "2":

        tsa = 6 * a * a

        print(
            "TSA =",
            clean(tsa)
        )

    elif choice == "3":

        csa = 4 * a * a

        print(
            "CSA =",
            clean(csa)
        )

    else:

        print("Invalid choice!")


# ================================================================
# CUBOID
# ================================================================

def shape_cuboid():

    print("\n--- CUBOID ---")

    length = get_positive_number(
        "Enter length: "
    )

    breadth = get_positive_number(
        "Enter breadth: "
    )

    height = get_positive_number(
        "Enter height: "
    )

    print("\nWhat do you want to calculate?")
    print("1. Volume")
    print("2. TSA")
    print("3. CSA")

    choice = input("Enter your choice: ")

    if choice == "1":

        volume = (
            length *
            breadth *
            height
        )

        print(
            "Volume =",
            clean(volume)
        )

    elif choice == "2":

        tsa = 2 * (
            length * breadth
            +
            breadth * height
            +
            height * length
        )

        print(
            "TSA =",
            clean(tsa)
        )

    elif choice == "3":

        csa = 2 * height * (
            length + breadth
        )

        print(
            "CSA =",
            clean(csa)
        )

    else:

        print("Invalid choice!")


# ================================================================
# CYLINDER
# ================================================================

def shape_cylinder():

    print("\n--- CYLINDER ---")

    r = get_positive_number(
        "Enter radius: "
    )

    h = get_positive_number(
        "Enter height: "
    )

    print("\nWhat do you want to calculate?")
    print("1. Volume")
    print("2. TSA")
    print("3. CSA")

    choice = input("Enter your choice: ")

    if choice == "1":

        volume = PI * r * r * h

        print(
            "Volume =",
            clean(volume)
        )

    elif choice == "2":

        tsa = 2 * PI * r * (r + h)

        print(
            "TSA =",
            clean(tsa)
        )

    elif choice == "3":

        csa = 2 * PI * r * h

        print(
            "CSA =",
            clean(csa)
        )

    else:

        print("Invalid choice!")


# ================================================================
# CONE
# ================================================================

def shape_cone():

    print("\n--- CONE ---")

    r = get_positive_number(
        "Enter radius: "
    )

    h = get_positive_number(
        "Enter height: "
    )

    # Slant height
    l = square_root(
        r * r + h * h
    )

    if l is None:

        print("Unable to calculate slant height.")
        return

    print(
        "Slant Height =",
        clean(l)
    )

    print("\nWhat do you want to calculate?")
    print("1. Volume")
    print("2. TSA")
    print("3. CSA")

    choice = input("Enter your choice: ")

    if choice == "1":

        volume = (
            PI * r * r * h / 3
        )

        print(
            "Volume =",
            clean(volume)
        )

    elif choice == "2":

        tsa = PI * r * (r + l)

        print(
            "TSA =",
            clean(tsa)
        )

    elif choice == "3":

        csa = PI * r * l

        print(
            "CSA =",
            clean(csa)
        )

    else:

        print("Invalid choice!")


# ================================================================
# SPHERE
# ================================================================

def shape_sphere():

    print("\n--- SPHERE ---")

    r = get_positive_number(
        "Enter radius: "
    )

    print("\nWhat do you want to calculate?")
    print("1. Volume")
    print("2. TSA")
    print("3. CSA")

    choice = input("Enter your choice: ")

    if choice == "1":

        volume = (
            4 * PI * r * r * r / 3
        )

        print(
            "Volume =",
            clean(volume)
        )

    elif choice == "2":

        tsa = 4 * PI * r * r

        print(
            "TSA =",
            clean(tsa)
        )

    elif choice == "3":

        # For a sphere, CSA = surface area
        csa = 4 * PI * r * r

        print(
            "CSA =",
            clean(csa)
        )

    else:

        print("Invalid choice!")


# ================================================================
# HEMISPHERE
# ================================================================

def shape_hemisphere():

    print("\n--- HEMISPHERE ---")

    r = get_positive_number(
        "Enter radius: "
    )

    print("\nWhat do you want to calculate?")
    print("1. Volume")
    print("2. TSA")
    print("3. CSA")

    choice = input("Enter your choice: ")

    if choice == "1":

        volume = (
            2 * PI * r * r * r / 3
        )

        print(
            "Volume =",
            clean(volume)
        )

    elif choice == "2":

        # TSA includes the circular base
        tsa = 3 * PI * r * r

        print(
            "TSA =",
            clean(tsa)
        )

    elif choice == "3":

        csa = 2 * PI * r * r

        print(
            "CSA =",
            clean(csa)
        )

    else:

        print("Invalid choice!")


# ================================================================
# SHAPE CALCULATOR MENU
# ================================================================

def shape_calculator():

    while True:

        print("\n")
        print("=" * 60)
        print("                 SHAPE CALCULATOR")
        print("=" * 60)

        print("\n--- 2D SHAPES ---")

        print("1. Circle")
        print("2. Square")
        print("3. Rectangle")
        print("4. Triangle")

        print("\n--- 3D SHAPES ---")

        print("5. Cube")
        print("6. Cuboid")
        print("7. Cylinder")
        print("8. Cone")
        print("9. Sphere")
        print("10. Hemisphere")

        print("\n0. Return to Main Calculator")

        choice = input(
            "\nEnter your choice: "
        )

        if choice == "1":

            shape_circle()

        elif choice == "2":

            shape_square()

        elif choice == "3":

            shape_rectangle()

        elif choice == "4":

            shape_triangle()

        elif choice == "5":

            shape_cube()

        elif choice == "6":

            shape_cuboid()

        elif choice == "7":

            shape_cylinder()

        elif choice == "8":

            shape_cone()

        elif choice == "9":

            shape_sphere()

        elif choice == "10":

            shape_hemisphere()

        elif choice == "0":

            print(
                "\nReturning to main calculator..."
            )

            break

        else:

            print(
                "\nInvalid choice!"
                "\nPlease select a valid option."
            )

        input(
            "\nPress ENTER to continue..."
        )


# ================================================================
# MAIN MENU
# ================================================================

def main_menu():

    while True:

        print("\n")
        print("=" * 70)
        print("             ADVANCED MATHEMATICS CALCULATOR")
        print("=" * 70)

        print("""
Choose the operation you want:

1.  Arithmetic Calculator
2.  Scientific Calculator
3.  Trigonometry
4.  Polynomial Calculator
5.  Complex Number Calculator
6.  Statistics
7.  Matrix Calculator
8.  Unit Conversion
9.  Number System Conversion
10. Degree / Radian Converter
11. Length Calculator
12. Constants (π and e)
13. Shape calculator
0.  Exit
""")

        choice = input("Enter your choice: ")

        print()

        if choice == "1":

            arithmetic_calculator()

        elif choice == "2":

            scientific_calculator()

        elif choice == "3":

            trigonometry()

        elif choice == "4":

            polynomial_calculator()

        elif choice == "5":

            complex_calculator()

        elif choice == "6":

            statistics_calculator()

        elif choice == "7":

            matrix_calculator()

        elif choice == "8":

            unit_conversion()

        elif choice == "9":

            number_conversion()

        elif choice == "10":

            print("1. Degree -> Radian")
            print("2. Radian -> Degree")

            option = input("Select: ")

            value = float(input("Enter value: "))

            if option == "1":

                print(
                    "Radian =",
                    clean(degree_to_radian(value))
                )

            elif option == "2":

                print(
                    "Degree =",
                    clean(radian_to_degree(value))
                )

            else:

                print("Invalid option.")

        elif choice == "11":

            length_calculator()

        elif choice == "12":

            print("π =", PI)
            print("e =", E)
            
        elif choice == "13":

            shape_calculator()
            
        elif choice == "0":

            print("\nThank you for using the")
            print("ADVANCED MATHEMATICS CALCULATOR!")
            print("Goodbye.")

            break

        else:

            print(
                "Invalid choice! "
                "Please select a number from the menu."
            )

        input("\nPress ENTER to return to the main menu...")


# ================================================================
# PROGRAM START
# ================================================================

print("=" * 70)
print("WELCOME TO THE ADVANCED MATHEMATICS CALCULATOR")
print("=" * 70)

print("""
This calculator is created using Python without
external libraries or modules.

You can perform arithmetic, scientific mathematics,
trigonometry, polynomial calculations, complex numbers,
statistics, matrices, unit conversion and number-system
conversion.

Select an option from the menu to begin.
""")

main_menu()

