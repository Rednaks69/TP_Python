s1 = "voici une phrase !"
s2 = s1.split(" ")
print(s2)
tab = s2[::-1]
print(tab)


def afficherInverse(s):
    return s[len(s)::-1]


for i in range(len(tab)):
    tab[i] = afficherInverse(tab[i])

print(tab)
