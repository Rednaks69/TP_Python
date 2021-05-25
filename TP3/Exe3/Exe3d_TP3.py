import math

epsilon = 20


def fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact


def puissance(x, n):
    puiss = 1
    for i in range(1, n+1):
        puiss *= x
    return puiss


def expo(x):
    for i in range(1, 101):
        if i <= epsilon:
            ex = abs(puissance(x, i)/fact(i))
    return ex


print(expo(3))
