####################################################################################################
# * Complement de TP python
# * made by : Azer Hasnaoui
# * classroom : GLSI-1
# * year : 2020-2021
####################################################################################################
#                     -Tuples-                                                                     #
####################################################################################################
# A tuple is a collection like Lists but it is ordered and unchangeable
# ? Summary
# ? -1- Creating a Tuple
# ? -2- Accessing List Elements
# ? -3- Counting List Elements
# ? -4- Update Tuples
# ? -5- Unpack Tuples
# ? -6- Loop Tuples
######################################################################################################
# * -1- Creating a Tuple
firstTuple = ("Ahmed", "FSB", "GLSI")
secondTuple = ("phelippe", 34, True, 40, "male")
print("FirstTuple is", firstTuple, "it have the type of ", type(firstTuple))
print("secondTuple is", secondTuple, "it have the type of ", type(secondTuple))
# Creating a tuple using a Constructor
thirdTuple = tuple(())  # double round-brackets
print("secondTuple is", secondTuple, "it have the type of ", type(secondTuple))

# * -2- Accessing List Elements
print("accessing to the first value ", firstTuple[0])
subtuple_1 = firstTuple[1:3]
print("slicing the tuple ", subtuple_1)
# * -3- Counting List Elements
sizeOffirstTuple = len(firstTuple)
sizeOfsubtuple_1 = len(subtuple_1)
print("the size of firstTuple is", sizeOffirstTuple)
print("the size of subtuple_1 is", sizeOfsubtuple_1)
# checking of Existence
print("FSB" in firstTuple)
if "male" in secondTuple:
    print("Exist in tuple")
# Counting Occurences
print("Nb of 'FSB' in tuple", firstTuple.count("FSB"))
# locating Elements
print(secondTuple.index(34))
# => list.index(x,i,j)  the search will start at index i and will stop at index j

# * -4- Update Tuples
# Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
# adding Items
# Once a tuple is created, you cannot add items to it. you can convert it into a list, add your item(s), and convert it back into a tuple.
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
# remove Items
# Tuples are unchangeable, so you cannot remove items from it. you can convert it into a list, add your item(s), and convert it back into a tuple.
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
# Delete
thistuple = ("apple", "banana", "cherry")
del thistuple


# * -5- Unpack Tuples
# extract the values back into variables
(name, university, classRoom) = firstTuple
print(name)
# // (name2) = secondTuple
# // print(name2)
# Using the Asterisk *
(name2, age, *others) = secondTuple
print(name2)
print(age)
print(others)
print(type(others))  # the type change automaticly to list


# * -6- Loop Tuples
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i = i + 1

for i in range(len(firstTuple)):
    print(firstTuple[i])
