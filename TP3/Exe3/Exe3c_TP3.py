x1 = 3


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


def expro(x):
    ex = 1
    for i in range(1, 101):
        ex += puissance(x, i)/fact(i)
    return ex


print(expro(x1))
