####################################################################################################
# * Complement de TP python
# * made by : Azer Hasnaoui
# * classroom : GLSI-1
# * year : 2020-2021
####################################################################################################
#                     -Sets-                                                                       #
####################################################################################################
# A set is a collection which is both unordered and unindexed.
# Set items can appear in a different order every time you use them, and cannot be referred to by index or key.
# ? Summary
# ? -1- Creating a Set
# ? -2- Accessing Set Elements
# ? -3- Counting Set Elements
# ? -4- Iterating Through Set Elements
# ? -5- Searching Elements within Sets
# ? -6- Adding and Deleting Elements
# ? -7- Set Operations (union , intersection, difference, Symmetric Difference)
######################################################################################################
# * -1- Creating a Set
firstSet = {"apple", "blackberry", "strawberry",
            "raspberry", "cloudberry", "blueberry"}
secondSet = set(("gojiberry", "barberry", "cowberry"))
print(firstSet)
print("type of fistlist", type(firstSet))
print(secondSet)
print("type of secondSet", type(secondSet))
# * -2- Accessing Set Elements
# Being unordered collections, it is not possible to identify an element within a set using
# an index or any other mechanism.
# * -3- Counting Set Elements
print(len(secondSet))

# * -4- Iterating Through Set Elements
S = set(range(0, 10, 3))
print("Value in S are\t", S)
for i in S:
    print("even", i) if i % 2 == 0 else print("odd", i)

# * -5- Searching Elements within Sets
if "apple" in (firstSet and secondSet):
    print("exist")
else:
    print("dont exist")

# * -6- Adding and Deleting Elements
# Adding Elements
S2 = set(range(0, 10, 2))
S2.add(11)
print(S2)
S.update(S2)
print(S)
# Deleting Elements
firstSet.remove("apple")
firstSet.discard("banana")
lastValue = firstSet.pop()
print(lastValue)
S.clear()
del S2

# * -7- Set Operations
# union function
firstSet.union(secondSet)
print(firstSet)
