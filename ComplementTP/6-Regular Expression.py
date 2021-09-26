####################################################################################################
# * Complement de TP python
# * made by : Azer Hasnaoui
# * classroom : GLSI-1
# * year : 2020-2021
####################################################################################################
#                     -Regular Expression-                                                         #
####################################################################################################
# ? Summary
# ? -1- Basic Regular Expression Operators
# ? -----1-1- Matching a Single Character
# ? -----1-1-----1 Matching any Character Using the . Operator
# ? -----1-1-----2 Matching a Character Within a Set Using the[] Operator
# ? -----1-1-----3 Matching a Character Within a Range of Characters Using the[-] Operator
# ? -----1-1-----4 Matching a Character Within a Negated Set Using the [ ^ ] Operator
# ? -----1-1-----5 Shortcut Escape Sequences for Characters
# ? -----1-2- Matching Multiple Characters
# ? -----1-2-----1 Matching 0 or More Occurrences using the * Operator
# ? -----1-2-----2 Matching 1 or More Occurrences using the + Operator
# ? -----1-2-----3 Matching 0 or 1 Occurrences using the ? Operator
# ? -----1-2-----4 Matching Multiple Occurrences using the {} Operator
# ? -----1-2-----5 Grouping Using the() Operator
# ? -----1-3- Matching Multiple Patterns Using the
# ? -----1-4- Anchoring Operators
# ? -----1-4-----1 Anchoring at the Beginning of a String
# ? -----1-4-----2 Anchoring at the End of a String Using the $ Operator
# ? -----1-4-----3 Anchoring at Word Boundaries
# ? -----1-4-----4 Negated Anchoring at Word Boundaries
# ? -2- Framing Regular Expressions in Python
# ? -----2-1 Dealing with Backslashes(\)
# ? -----2-2 Using Raw Literals for RE
# ? -----2-3 Practical Examples of RE
# ? -----2-3-----1 RE for Name
# ? -----2-3-----2 RE for Username
# ? -----2-3-----3 RE for Password
# ? -----2-3-----4 RE for Date of Birth
# ? -----2-3-----5 RE for Phone
# ? -----2-3-----6 RE for Email
# ? -----2-3-----7 RE for IP Address
# ? -----2-3-----8 RE for Integers
# ? -----2-3-----9 RE for Real Numbers
# ? -----2-3-----10 RE for Coordinates
# ? -3- Searching Strings Using match(), fullmatch() and search()
# ? -----3-1 The search() Function
# ? -----3-2 The fullmatch() Function
# ? -----3-3 The match() Function
# ? -----3-4 Flags for Dealing with Regular Expressions
# ? -4- Working With Groups
# ? -----4-1 Simple Group Content Extraction
# ? -----4-2 Back-Reference Contents
# ? -----4-3 Nested Groups
# ? -5- Working with Matches
# ? -----5-1 Extracting the Original String and RE
# ? -----5-2 Extracting the Group Contents
# ? -----5-3 Extracting the Group Locations
# ? -----5-4 Expanding a Template String
# ? -6- Locating Matches Using findall() and finditer()
# ? -7- Splitting Strings Using split()
# ? -8- Replacing Strings Using sub() and subn()
# ? -9- Compiling Regular Expressions
####################################################################################################
# * -1- Basic Regular Expression Operators
# * -----1-1- Matching a Single Character
# * -----1-1-----1 Matching any Character Using the . Operator
#   The . operator matches any one character
# the RE n.t matches those strings that contain an n, followed by any one nonnewline character, followed by t.

# * -----1-1-----2 Matching a Character Within a Set Using the[] Operator
# The[] operator is similar to the . operator – it is also a placeholder for a single
# character, except that the character is restricted to be one amongst the characters
# listed within the[].

# the RE n[aeiou]t will match any string containing n that is followed by a lowercase vowel followed by t.

# * -----1-1-----3 Matching a Character Within a Range of Characters Using the[-] Operator
# To specify a range of characters within[], we can use the – operator within[].
# Thus, [a-e] represents any one character out of a, b, c, d and e. [4-6] represents
# any one character out of 4, 5 and 6.

# This can also be combined with the previous form. Thus, [a-emx-z] can match any
# of a, b, c, d, e, m, x, y and z.

# The RE n[a-e]t can match any string that contains n followed by any one of a, b, c, d and e followed by t.
