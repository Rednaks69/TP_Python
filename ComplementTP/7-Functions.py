import math
import sys
####################################################################################################
# * Complement de TP python
# * made by : Azer Hasnaoui
# * classroom : GLSI-1
# * year : 2020-2021
####################################################################################################
#                     -functions-                                                                  #
####################################################################################################
# ? Summary
# ? -1- Function Definition
# ? -2- Function Call
# ? -3- Positional Arguments
# ? -4- Default Arguments
# ? -5- Keyword Arguments
# ? -----5-1- Keyword Arguments for Positional Arguments
# ? -----5-2 Keyword Arguments for Default Arguments
# ? -6-  Variable Arguments
# ? -----6-1- Variable Arguments With Positional Parameters
# ? -----6-2- Variable Arguments With Default Arguments
# ? -----6-3- Variable Arguments Followed by Default Arguments
# ? -----6-4- Variable Arguments Followed by Keyword Arguments
# ? -7- Returning From Functions
# ? -8- Returning Single Values From Functions
# ? -9- Returning Collections From Functions
# ? -----9-1- Returning Tuples From Functions
# ? -----9-2- Returning Lists From Functions
# ? -----9-3- Returning Dictionaries From Functions
# ? -10- Global VariablesGlobal Variables
# ? -11- Nested Functions
# ? -----11-1- Inner Functions for Private Use
# ? -----11-2- Outer Functions for Abstraction
# ? -----11-3- Outer Functions as Generators
# ? -12- Lambda Expressions
# ? -----12-1- Anonymous functions
# ? -----12-2- Lambda
# ? -13- Unpacking Argument Lists
####################################################################################################
# * -1- Function Definition
"""
def function_name(parameters):
    function_body
    ...
"""

# * -2- Function Call


def hi():
    print("Hello World")


hi()

# * -3- Positional Arguments


def sum(x, y):
    print(x+y)


sum(2, 3)

# * -4- Default Arguments


def f(x, y, c=20, z=10):
    print(x, y, c, z)


f(1, 2, 30)

# * -5- Keyword Arguments
"""
Keyword arguments are special arguments where the parameter name is identified at
the place of call along with the value. These have various applications as shown in the
following subsections.
"""
# * -----5-1- Keyword Arguments for Positional Arguments


def argPosition(p, t, r):
    print("Interest:", (p*t*r)/100)


argPosition(1000, 3, 9.5)
# Interest: 285.0
argPosition(p=1000, r=9.5, t=3)
# Interest: 285.0
argPosition(1000, r=9.5, t=3)
# Interest: 285.0

# * -----5-2 Keyword Arguments for Default Arguments


def f(a, b, c=2, d=3):
    print(a, b, c, d)


f(10, 20, 30)
# 10 20 30 3
f(10, 20, d=30)
# 10 20 2 30


def f(a, b, c=2, d=3):
    print(a, b, c, d)


# f(1, 2, k=9)
#! TypeError: f() got an unexpected keyword argument 'k'

# dictionary
def f(a, b, **x):
    print(a, b)
    for k, v in x.items():
        print("The value of {} is {}".format(k, v))
    print(x)


f(1, 2, c=2, d=3)


# * -6-  Variable Arguments
# liste
def sum(*x):
    s = 0
    for i in x:
        s += i
    print(s)


sum(2, 3)
sum(2, 3, 5, 5, 5, 5)

# * -----6-1- Variable Arguments With Positional Parameters


def sum(a, b, *x):
    s2 = a+b
    for i in x:
        s2 += i
        print(s2)


sum(2, 3)

# * -----6-2- Variable Arguments With Default Arguments


def sum(a, b=100, *x):
    s = a+b
    for i in x:
        s += i
    print(s)


sum(5)
# 105
sum(5, 8)
# 13
sum(5, 8, 12)
# 25

# * -----6-3- Variable Arguments Followed by Default Arguments
print(1, 2, 3, sep=':', end='\n*****\n')
# 1: 2: 3
# *****


def sum(*x, negate=False):
    s = 0
    for i in x:
        s += i
    if negate:
        s = -s
    print(s)


sum(2, 3, 4)
# 9
sum(2, 3, 4, negate=True)
# -9
sum(2, 3, 4, True)
# 10


# * -----6-4- Variable Arguments Followed by Keyword Arguments
def sum(a, b=2, *c, **d):
    print("a:", a, "b:", b)
    print("c:", end='')
    for i in c:
        print(i, end=' ')
    print("\nd:", end='')
    for k, v in d.items():
        print("({}={})".format(k, v), end='')
    print()


sum(1, 2, 3, 4, 5, 6, 7, x=2, y=4, z=9)
# a: 1 b: 2
# c: 3 4 5 6 7
# d: (x=2)(y=4)(z=9)

# * -7- Returning From Functions


def hi():
    print("Hello World")
    return
    print("Heya!")

# * -8- Returning Single Values From Functions


def hi():
    return"Hello World"


hi()


def sum(x, y):
    return x+y


sum(3, 7)


# * -9- Returning Collections From Functions
# * -----9-1- Returning Tuples From Functions
def calc(x, y):
    return (x+y, x-y, x*y, x/y)


result = calc(2, 3)
print(result)
print("Sum=", result[0], "difference=", result[1])

# * -----9-2- Returning Lists From Functions


def calc(x, y):
    return [x+y, x-y, x*y, x/y]


result = calc(2, 3)
print(result)
print("Sum=", result[0], "difference=", result[1])

# * -----9-3- Returning Dictionaries From Functions


def calc(x, y):
    return {'sum': x+y, 'diff': x-y, 'prod': x*y, 'quot': x/y}


result = calc(2, 3)
print(result)
print("Sum=", result['sum'], "difference=", result['diff'])


# * -10- Global VariablesGlobal Variables
x = 2


def f():
    x = 3
    print(x)


print(x)
f()

# *** *** *** *** *** *** ***


def f():
    global x
    x = 3
    print(x)


print(x)
f()
print(x)

# * -11- Nested Functions


def f():
    print("This is f")

    def g():
        print("This is g")
    g()


f()
# * -----11-1- Inner Functions for Private Use


def gcd(x, y):
    def getPrimeFactors(n):
        factors = []
        factor = 2
        while n > 1:
            while n % factor == 0:
                factors.append(factor)
                n /= factor
            factor = factor+1
        return factors
    factors1 = getPrimeFactors(x)
    factors2 = getPrimeFactors(y)
    gcd = 1
    for i in factors1:
        if i in factors2:
            factors2.remove(i)
            gcd *= i
    return gcd


# x, y = input("Enter 2 integers:").split('')
# z = int(input("Enter integer: x"))
# q = int(input("Enter integer: y"))
# print("The GCD of {} and {} is {}".format(z, q, gcd(z, q)))

# * -----11-2- Outer Functions for Abstraction


def isPrime(n):
    def implIsPrime(n):
        for i in range(2, int(n/2)+1):
            if n % i == 0:
                return False
        return True
    if n < 0:
        print("Negative integer specified!")
    elif n == 0:
        print("Zero given!")
    elif n == 1:
        print("1 is neither prime nor composite!")
    else:
        return implIsPrime(n)
    sys.exit()


# try:
#     n = int(input("Enter a positive integer: "))
# except:
#     EOFError as e:
#     print(e)

# if isPrime(n):
#     print("Prime")
# else:
#     print("Composite")

# * -----11-3- Outer Functions as Generators


def power(n):
    def implPower(x):
        return int(math.pow(x, n))
    return implPower


# square = power(2)
# cube = power(3)
# print("Equation: ax^3 + bx^2 + cx + d")
# a, b, c, d = input("Enter the values of a, b, c, d:").split(' ')
# a, b, c, d = int(a), int(b), int(c), int(d)
# x = int(input("Enter the value of x:"))
# result = a*cube(x) + b*square(x) + c*x + d
# print("Result:", result)

# * -12- Lambda Expressions
# * -----12-2- Lambda
"""
    lambda parameters: expression
"""
# square=lambda x: x**2
# print(square(4))


# remainder = lambda num: num % 2
# print(remainder(5))

def testfunc(num):
    return lambda x: x * num


result1 = testfunc(10)
result2 = testfunc(100)
print(result1(9))
print(result2(4))

# * -13- Unpacking Argument Lists
"""
The *collection syntax expands the collection into arguments that can
either map on to corresponding parameters of a function or can be received
as variable arguments using the *args syntax
"""


def calc(x, y):
    return (x+y, x-y, x*y, x/y)


L = [2, 3]
calc(*L)
# (5, -1, 6, 0.6666666666666666)

"""
The **dictionary syntax expands the dictionary into keyword arguments
that can either map on to corresponding named parameters of a function or
can be received as additional keyword arguments using the **kargs syntax
"""


def calc(x, y):
    return (x+y, x-y, x*y, x/y)


D = {'x': 2, 'y': 3}
calc(**D)
# (5, -1, 6, 0.6666666666666666)


# * -14- Documentation Strings

def isPrime(n):
    """
        Returns whether n is prime or not.
        Given a non-negative integer n, this function
        returns True if n is prime and False otherwise.
        The argument n is assumed to be a positive integer
        greater than 1 (since 1 is neither prime nor composite).
        No argument validation is performed.
    """
    for i in range(2, int(n/2)+1):
        if n % i == 0:
            return False
    return True


print(isPrime.__doc__)


####################################################################################################
# * ░░░░░░░░░░░░░░░░░░░░░░█████████░░░░░░░░░ #
# * ░░███████░░░░░░░░░░███▒▒▒▒▒▒▒▒███░░░░░░░ #
# * ░░█▒▒▒▒▒▒█░░░░░░░███▒▒▒▒▒▒▒▒▒▒▒▒▒███░░░░ #
# * ░░░█▒▒▒▒▒▒█░░░░██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░░ #  # * Complement de TP python
# * ░░░░█▒▒▒▒▒█░░░██▒▒▒▒▒██▒▒▒▒▒▒██▒▒▒▒▒███░ #  # * made by : Azer Hasnaoui
# * ░░░░░█▒▒▒█░░░█▒▒▒▒▒▒████▒▒▒▒████▒▒▒▒▒▒██ #  # * classroom : GLSI-1
# * ░░░█████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██ #  # * year : 2020-2021
# * ░░░█▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒██ #
# * ░██▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒██▒▒▒▒▒▒▒▒▒▒██▒▒▒▒██ #
# * ██▒▒▒███████████▒▒▒▒▒██▒▒▒▒▒▒▒▒██▒▒▒▒▒██ #
# * █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒████████▒▒▒▒▒▒▒██ #
# * ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░ #
# * ░█▒▒▒███████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░░░ #
# * ░██▒▒▒▒▒▒▒▒▒▒████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█░░░░░ #
# * ░░████████████░░░█████████████████░░░░░  #                                              # *  END
####################################################################################################
