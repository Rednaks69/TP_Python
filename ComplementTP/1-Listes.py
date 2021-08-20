####################################################################################################
# * Complement de TP python
# * made by : Azer Hasnaoui
# * classroom : GLSI-1
# * year : 2020-2021
####################################################################################################
#                     -Lists-                                                                      #
####################################################################################################
# A list in Python is defined as an ordered sequence of elements that can be dynamically altered.
# ? Summary
# ? -1- Creating a lists
# ? -2- Accessing List Elements
# ? -3- Counting List Elements
# ? -4- Iterating Through List Elements
# ? -----4-1- Searching Elements within Lists
# ? -----4-2- Checking for Existence
# ? -----4-3- Counting Occurrences
# ? -----4-4- Locating Elements
# ? -5- List Slices
# ? -6- Adding and Deleting Elements
# ? -----6-1- Appending Elements
# ? -----6-2- Inserting Elements
# ? -----6-3- Deleting Elements
# ? -----6-4- Adding, Multiplying and Copying Lists
# ? -7- List Comprehension
# ? -8- Others Functions (sort, join, reverse ....)
######################################################################################################
# * -1- Creating a lists
firstList = ["apple", "banana", "2"]
print("the firstlist is ", firstList)
print("the type of the firstlist is ", type(firstList))
list2 = [64, False, "40", "male"]   # different data type
# List Constructor
# -- the double round-brackets list((Items))
MyList = list(("apple", "banana", "2", False, "88"))
MyList2 = list(())
print("Myliste created by constructor", MyList)
print("Myliste2 created by constructor", MyList2)
# * -2- Accessing List Elements
print("item in index 0 of firstList is", firstList[0])
print("item in index 1 of firstList is", firstList[1])
print("item in index -1 of firstList is", firstList[-1])
print("item in index -2 of firstList is", firstList[-2])
list3 = [6, 4, 5, 7]
print("item in index 0 of list3 is", list3[0])
list3[0] = list3[1]+list3[2]
print("item in index 0 of list3 after the adding is", list3[0])

# * -3- Counting List Elements
# The len() function
print("the size of the firstlist is ", len(firstList))
print("the size of the list2 is ", len(list2))

# * -4- Iterating Through List Elements
print("-----4-1-0- Iterating Through List Elements")
print("Iterating of firstList")
for i in firstList:
    print(i)
print("Iterating of list2")
for i in list2:
    print(i)


# * -----4-1- Searching Elements within Lists
# * -----4-1-1- Checking for Existence
print("-----4-1-1- Checking for Existence")
# The "in" and "not in" operators help us to verify whether a particular element is present in a list or not.
if "apple" in firstList:
    print("apple exist in firstList")

if "berry" not in firstList:
    print("berry dont exist in firstList")

# * -----4-1-2- Counting Occurrences
print("-----4-1-2- Counting Occurrences")
# The count() member function of list tells us how many instances of the specified object is present in the list.
print(firstList.count("apple"))
print(MyList.count("banana"))

# * -----4-1-3-  Locating Elements
print("-----4-1-3-  Locating Elements")
# The index() member function of list searches for the first occurrence of an element
# within a list and returns the index where it was found, and throws a ValueError if
#not found
print(firstList.index("apple"))
print(MyList.index("banana"))
# list.index(x,i,j)  the search will start at index i and will stop at index j

# * -5- List Slices
# A list slice uses syntax namelist[start:end]
# start is the starting index from where to start extracting elements and end is the ending index(excluding end)
# Start default value is 0 and end default value is len(list)
print("-5- List Slices")
subliste2 = list2[1:3]  # creating a sublist
print(subliste2)
print(type(subliste2))  # the type of a sublist is a list
# Start default value is 0 and end default value is len(list)
print(MyList[:3])
print(firstList[1:])
#  We can use list slices to modify the contents of a list
print('Mylist before modification\n\t', MyList)
MyList[1:3] = ["allo", False]
print("Mylist After No size modification \n\t", MyList)
MyList[1:3] = ["allo", False, True, 4, object()]
print("Mylist After  size modification \n\t", MyList)
# insert contents
print('firstList before modification \n\t', firstList)
firstList[1:1] = ["allo", False, True, 4]
print('firstList after insert modification \n\t', firstList)
#  We can use list slices to delete contents of a list
MyList[4:7] = ["hello world"]
print('Mylist after deleting contents modification \n\t', MyList)
# clear contents
firstList[:] = []
print("clear contents modification result, firstList is ", firstList)
# there is a third variable in list slice and its the step
subliste3 = MyList[1:4:2]
print("list slice with step", subliste3)


# * -6 - Adding and Deleting Elements
# * -----6-1 - Appending Elements
print("-6 - Adding and Deleting Elements \n -----6-1 - Appending Elements")
# To add one or more elements to the end of a list we use the syntax namelist.append(x)
# list.append(x) is similar to namelist[len(list):]=[x]
MyList.append("hello again")
print("Mylist After  append modification \n\t", MyList)
# namelist.extend(list), combine two list together
# namelist.extend(L) is similar to list[len(list):]=L
firstList.extend(MyList)
firstList.extend(list2)
print("firstList after entend modification \n\t", firstList)

# * -----6-2- Inserting Elements
print("-----6-2- Inserting Elements")
# To add elements at any desired location within the list, the list.insert(i,x)
# function can be used, which inserts the element x at index i
firstList.insert(1, object())
print("firstList after insert function modification \n\t", firstList)

# * -----6-3- Deleting Elements
print("-----6-3- Deleting Elements")
del firstList[1:4]
print("firstList after delete function modification \n\t", firstList)
del firstList  # will delete the entire list
# function remove
MyList.remove('88')
print("Mylist After remove modification \n\t", MyList)
# function pop
MyList.pop()
print("Mylist After pop modification \n\t", MyList)
MyList.pop(2)
print("Mylist After pop modification with index \n\t", MyList)
# function clear
MyList.clear()
print("Mylist After clear modification with \n\t", MyList)

# * -----6-4- Adding, Multiplying and Copying Lists
print("-----6-4- Adding, Multiplying and Copying Lists")
print("list2 is \n\t", list2, "\n", "list3 is \n\t", list3)
# Adding
listConcat = list2 + list3
print("the result of the addition is ", listConcat)
# L1 += L2 is similar to L1.extend(L2)

# Multiplying Lists
listMultip = list2 * 2
print("the result of the multiplication is ", listMultip)

# Copying Lists
listCopie = list2.copy()
print("the result of the copying ", listCopie)

# * -7- List Comprehension
print("-7- List Comprehension")
# shortcut
# Syntax -> newlist = [EXPRESSION for ITEM in ITERABLE if CONDITION == True]
# if we have this statement
fruits = ["apple", "banana", "berry"]
newlist = []
for i in fruits:
    if "a" in i:
        newlist.append(i)

print(newlist)
# We can make it shorter by applying the List Comprehension
newlist_Compreh = [item for item in fruits if "a" in item]
print(newlist_Compreh)
newlist_Compreh_2 = [item.upper() for item in fruits if "b" in item]
print(newlist_Compreh_2)
# The expression containing conditions
newlist_Compreh_3 = [item if item !=
                     "apple" else "orange" for item in fruits if "a" in item]
print(newlist_Compreh_3)

# * -8- Others Functions
# Sorting a List
fruits.sort()
print("after sort modification \t ", fruits)
fruits.sort(reverse=True)
print("after sort reverse modification \t ", fruits)


# ---- costomize sorting
def myfunc(n):
    return pow(n, 2)


listNumeric = [10, 5, 7]
listNumeric.sort(key=myfunc)
print(listNumeric)
# Reversing a List
listNumeric.reverse()
print("after reverse function modification \t ", listNumeric)
# min and max
maxList = max(listNumeric)
minListe = min(listNumeric)
print("le max dans listNumeric is", maxList,
      "\nle min dans listNumeric is", minListe)

# Using the Asterisk *
testList = list((1, 2, 3, 4))
print(testList)
(one, two, *other) = testList
print(two)
print(other)
print(type(other))

####################################################################################################
####################################################################################################
# * Complement de TP python
# * made by : Azer Hasnaoui
# * classroom : GLSI-1
# * year : 2020-2021
#!  END
####################################################################################################
