####################################################################################################
# * Complement de TP python
# * made by : Azer Hasnaoui
# * classroom : GLSI-1
# * year : 2020-2021
####################################################################################################
#                     -Dictionaries-                                                               #
####################################################################################################
# A dictionary is a collection of key-value pairs subject to the constraint that all the keys
#                                                                           should be unique.
# The keys of a dictionary can be considered to be members of a set ( and are thus unique),
#                                                            with each key keeping track of a value.
# ? Summary
# ? -1- Creating a Dictionarie
# ? -2- Accessing Dictionarie Elements
# ? -3- Counting Dictionarie Elements
# ? -4- Iterating Through Dictionarie Elements
# ? -5- Searching Elements within Dictionarie
# ? -6- Adding and Deleting Elements
####################################################################################################
# * -1- Creating a Dictionarie
d = dict([('car', 'red'), ('taxi', 'yellow')])
print(d)
print(type(d))

D = {'apple': "red", 'salaire': 'null', 'mango': 'green', 'grapes': 'green'}
print(D)
print(type(D))

# * -2- Accessing Dictionarie Elements
print(D['apple'])
# print(D['banana'])
D['apple'] = 'green'
D['strawberry'] = 'brightRed'
print(D)

# * -3- Counting Dictionarie Elements
print(len(D))
print(len(d))

# * -4- Iterating Through Dictionarie Element
for k in D:
    print(k)

for i in d.keys():
    print(i)

for j in d.values():
    print(j)
# for j in d:
#     print(d[j])

for i, j in d.items():
    print(i, j)

# * -5- Searching Elements within Dictionarie
if "apple" in d:
    print("True")
else:
    print("False")

print("car" in d)
print("iceCream" not in d)

# * -----5-1 - dict.get()
print(D.get("apple"))
print(D.get("melow"))

# * -----5-2 - Extracting All Keys With a Particular Value
v = 'green'
for k in D:
    if D[k] == v:
        print(k)


# * -6- Adding and Deleting Elements
# * -----6-1 -Adding Elements Using[]
print('bleuberry' in D)
D['bleuberry'] = 'bleu'
print('bleuberry' in D)

# * -----6-2 -Adding Elements using setdefault()
D.setdefault("pear")
D.setdefault('melon', 'yellow')
print(D)

# * -----6-3 - Delete an Element

del D['apple']
print(D.popitem())
print(D.pop('strawberry'))
print(D)
print(D.pop("strawberry", 'default'))
print(D)
D.clear()
print(D)
