s1 = "hello again"


def occurrence(s, occ):
    sumocc = 0
    for i in range(len(s)):
        if occ == s[i]:
            sumocc += 1

    return sumocc


print("Le nombre d'occurence", occurrence(s1, "l"))
