def maxList(myList):
    return max(myList)


def maxListFor(mylist):
    maximaum = myList[0]
    for i in mylist:
        if i > maximaum:
            maximaum = i
    return maximaum


myList = [1, 5, 2, 8, 9, 100, 4, 0]
print(maxList(myList))
print(maxListFor(myList))
