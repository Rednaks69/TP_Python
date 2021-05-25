# del = b**2 - 4 a * c
# del > 0  => x1 = -b + sqrt(del)/ 2a
#  x2 = -b - sqrt(del)/ 2a
# del == 0 => -b/2a
# del < 0  => impossible
from math import sqrt


def Resoudre(a, b, c):
    delta = b**2 - 4 * a * c
    if delta > 0:
        x1 = -b + sqrt(delta) / 2*a
        x2 = -b - sqrt(delta) / 2*a
        print(" le resolistion de lequation est : x1 = %f, x2 = %f" % (x1, x2))

    elif delta == 0:
        x = -b/2*a
        print(" le resolistion de lequation est : x = ", x1)
    else:
        print(" solution impossible")
        exit()


a1 = 2
b1 = 10
c1 = 3
Resoudre(a1, b1, c1)
