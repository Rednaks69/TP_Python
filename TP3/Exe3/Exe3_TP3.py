import math


n = 4
fact = 1


for i in range(1, n+1):
    fact *= i
print(" le factorielle de n = ", fact)

print(" le 2emme fact est : ", math.factorial(4))


def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)


print(" fontion fact est : ", fact(4))
