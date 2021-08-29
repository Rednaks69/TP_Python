from string import Template
#*##################################################################################################
# * Complement de TP python
# * made by : ▞▚ ▜▙ █☰ 🆁 █▬█ ▞▚ ▟▛ ▛▟ ▞▚ ██ ▙▟ █                          # ──▒▒▒▒▒▒─
# * classroom : GLSI-1                                                     # ─▒─▄▒─▄▒─
# * year : 2020-2021                                                       # ─▒▒▒▒▒▒▒─
# *##############################                                          # ─▒▒▒▒▒▒▒─
# *           -String-         *#                                          # ─▒─▒─▒─▒─
#*##################################################################################################

# ? Summary
# ? -1- Checking For the Existence of a Substring
# ? -----1-1- Using startswith() and endswith()
# ? -----1-2- Using find(), rfind(), index() and rindex()
# ? -2- Counting Occurrences with count()
# ? -3- Splitting Strings
# ? -----3-1- Using partition() and rpartition()
# ? -----3-2- Using split() and lstrip(), rsplit()
# ? -----3-3- Using splitlines()
# ? -4- Joining Strings using join()
# ? -5- Modifying Strings
# ? -----5-1- Stripping Strings Using lstrip(), rstrip() and strip()
# ? -----5-2- Replacing Substrings Using replace()
# ? -----5-3- Substituting Substrings Using Template Strings
# ? -----5-3-----1 Substituting Values in a Template Using substitute()
# ? -----5-3-----2 Substituting Values in a Template Using safe_substitute()
# ? -----5-4- String Translation Using maketrans() and translate()
# ? -6- Padding Strings
# ? -----6-1- Justifying a String
# ? -----6-1- Filling a String Using zfill()
# ? -----6-1-Expanding Tabs in a String Using expandtabs()
# ? -7- Formatting Strings
####################################################################################################
# * -1- Checking For the Existence of a Substring
# * -----1-1- Using startswith() and endswith()

"""
    str.startswith(substring)
    str.startswith(substring,start)
    str.startswith(substring,start,end)
"""

"""
    str.endswith(substring)
    str.endswith(substring,start)
    str.endswith(substring,start,end)
"""
# * -----1-1-1 Using startswith()
print("** Using startwith() **")

firstString = "This is my first String"

print(firstString.startswith('This'))
# passing a tuple instead of a single string
print(firstString.startswith(('This', 'this')))  # true
print(firstString.startswith(('This', 'thAT')))  # true
# the code will search if first string OR the second is the start of your string

print(firstString.startswith("is"))  # fasle
print(firstString.startswith("is", 2))  # true
print(firstString.startswith(("this", "is", "that"), 5))  # true
print(firstString.startswith("is", 5, 6))  # fasle

# * -----1-1-2 Using  endswith()
print("** Using endswith() **")
print(firstString.endswith('string'))  # fasle
print(firstString.endswith(('string', 'String')))  # true
print(firstString.endswith("String", 10, 13))  # fasle

# * -----1-2- Using find(), rfind(), index() and rindex()
# find() search the first occurence and return his index
if firstString.find("is") != -1:
    print("this substring exist")
else:
    print("find function will return -1")
# find() can be used to obtain all occurences in a string and return all the indexes within the use of
# find(subString, start)


secondString = "this programme is easy to learn"
substring = "is"
index = -1
indices = []
while True:
    index = secondString.find(substring, index+1)  # recurcive search
    print(index)
    if index == -1:
        break
    indices.append(index)

print(secondString)
col = 0
for i in indices:
    print(' '*(i-col), end='')
    print('^', end='')
    col = i+1
print()

# *----- rfind()
# str.rfind(substring,start,end)

index = len(secondString)-len(substring)+1
indices = []
while True:
    index = secondString.rfind(substring, 0, index+len(substring) - 1)
    if index == -1:
        break
    indices.append(index)
print(secondString)
col = 0

for i in reversed(indices):
    print(' '*(i-col), end='')
    print('^', end='')
    col = i+1
print("\n\n")

# * -2- Counting Occurrences with count()

"""
    str.count(substring)
    str.count(substring,start)
    str.count(substring,start,end)
"""

# * -3- Splitting Strings
# * -----3-1- Using partition() and rpartition()
print("----* Splitting Strings *----")
"""
    str.partition(separator)
    str.rpartition(separator)
"""
theerdString = "my name is : azer"
print(theerdString.partition(":"))

# * -----3-2- Using split() and lstrip(), rsplit()
""""
    str.split()
    str.split(separator)
    str.split(separator,maxsplits)
"""

# * -4- Joining Strings using join()
print("\n\n----* Joining Strings *----")
"""
    str.join(iterable)
"""
forthString = " parsing JSON"
fithString = " is made made by a fetch"

print(forthString.join(("", fithString)))
print("->".join((forthString, fithString)))

# * -5- Modifying Strings
# * -----5-1- Stripping Strings Using lstrip(), rstrip() and strip()
"""
    str.lstrip()
    str.lstrip(chars)
"""
""""
    str.rstrip()
    str.rstrip(chars)
"""
""""
    str.strip()
    str.strip(chars)
"""

exempString = " \t\r\nHello \t\r\n "
print(exempString.lstrip())

exempString = "233Hello466World599"
print(exempString.lstrip("123456789"))

exempString = "233Hello466World599"
print(exempString.rstrip("123456789"))

exempString = " \t\r\nHello \t\r\n "
print(exempString.strip())


# * -----5-2- Replacing Substrings Using replace()
"""
    str.replace(old,new)
    str.replace(old,new,count)
"""
print("kyoto-Bombay-shenzhen-Bombay".replace("Bombay", "Mumbai"))
print("kyoto-Bombay-shenzhen-Bombay".replace("Bombay", "Mumbai", 1))

# * -----5-3- Substituting Substrings Using Template Strings
# * -----5-3-----1 Substituting Values in a Template Using substitute()
"""
    template.substitute(dict)
    template.substitute(keyargs)
    template.substitute(dict,keyargs)
"""
t = Template("The sum of $x and $y is $z")
d = dict(x=10, y=20, z=30)
print(t.substitute(d))
print(t.substitute(dict(x=2, y=12, z=14, a=100)))

# * -----5-3-----2 Substituting Values in a Template Using safe_substitute()
# dont generate error
t = Template("The sum of $x and $y is $z")
t.safe_substitute(dict(x=2), z=100)  # Result: 'The sum of 2 and $y is 100'

# * -----5-4- String Translation Using maketrans() and translate()
"""
    str.maketrans(dict)
    str.maketrans(lookup,replacement)
    str.maketrans(lookup,replacement,discard)
"""
d = {'1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e',
     '6': 'f', '7': 'g', '8': None, '9': None}
t = str.maketrans(d)
res = "hello 0468 world".translate(t)  # 'hello 0df world'
print(res)

t = str.maketrans("aeiou", "AEIOU")
res = "This is a demonstration".translate(t)  # 'ThIs Is A dEmOnstrAtIOn'
print(res)

t = str.maketrans("aeiou", "AEIOU", " ")
res = "This is a demonstration".translate(t)  # 'ThIsIsAdEmOnstrAtIOn'
print(res)

# * -6- Padding Strings
# # * -----6-1- Justifying a String
# ljust() - to left justify the content within an expanded string
"""
    str.ljust(width)
    str.ljust(width, fill)
"""
s = "Hello"
r = s.ljust(20)
print(r, "world")

r = s.ljust(20, "=")
print(r, "world")

# rjust() - to right justify the content within an expanded string
"""
    str.rjust(width)
    str.rjust(width, fill)
"""

s = "Hello"
r = s.rjust(20)
print(r, "world")

r = s.rjust(20, "=")
print(r, "world")

# center() - to center justify the content within an expanded string
"""
    str.center(width)
    str.center(width, fill)
"""
s = "Hello"
r = s.center(20)
print(r, "world")

r = s.center(20, "=")
print(r)

# * -----6-1- Filling a String Using zfill()
"""
    str.zfill(width)
"""
print("AA".zfill(5))
print("HAHA".zfill(5))

# * -----6-1-Expanding Tabs in a String Using expandtabs()
print("a\tb\t\tc".expandtabs())


# * -7- Formatting Strings
"""
    {argumentNumber: argumentFormat}
    {argumentName: argumentFormat}
"""
#?######################################################################
# ?   The complete syntax of the argumentFormat is shown below:         # ──▄█▀█▄─────────██
# ?   [[fill]align][sign][  # ][0][width][grouping][.precision][type]   # ▄████████▄───▄▀█▄▄▄▄
# ?                                                                     # ██▀▼▼▼▼▼─▄▀──█▄▄
# ?                                                                     # █████▄▲▲▲─▄▄▄▀───▀▄
# ?                                                                     # ██████▀▀▀▀─▀────────▀▀

# * -7----------1  Format Types
# * -7----------1----1 Format Types for Integers
print('{}'.format(15))          # Default format for integer
print('{:d}'.format(15))        # Decimal format for integer
print('{:b}'.format(15))        # Binary format for integer
print('{:x}'.format(15))        # Hexadecimal (Lowercase) format for integer
print('{:X}'.format(15))        # Hexadecimal (Uppercase) format for
print('{:n}'.format(15000))     # Numeric (Locale-Specific) format for integer
print('{:c}'.format(65))        # Character Format (A=ASCII 65)

# * -7----------1----2 Format Types for Real Numbers
print('{:f}'.format(12.165))    # Fixed Point Format
print('{:e}'.format(12.165))    # Exponentiation Format   '1.216500e+01'
print('{:E}'.format(12.165))    # Exponentiation Format   '1.216500E+01'
print('{:g}'.format(12.165))    # General Format          '12.165'
print('{:n}'.format(12.165))    # Numeric Format          '12.165'
print('{:%}'.format(12.165))    # Percentage Format       '1216.500000%'

# * -7----------2  Format Width
print('{:3d}'.format(2))  # 1-digit number with field width of 3   ' 2'
print('{:3d}'.format(12))  # 2-digit number with field width of 3   ' 12'
print('{:3d}'.format(1234))  # 4-digit number with field width of 3 '1234'

# * -7----------3 Format Alignment
print('{:<10}'.format(12))  # Left-align "12" in 10 columns    '12 '
print('{:>10}'.format(12))  # Right-align "12" in 10 columns  ' 12'
print('{:^10}'.format(12))  # Center-align "12" in 10 columns ' 12 '
print('{:=10}'.format(12))  # Right-align "12" in 10 columns, sign first  ' 12'
print('{:=10}'.format(-12))
# Right-align "-12" in 10 columns, sign first '- 12'
print('{:*<10}'.format(12))  # Left-align "12" in 10 columns '12********'
print('{:*>10}'.format(12))  # Right-align "12" in 10 columns '********12'
print('{:*^10}'.format(12))  # Center-align "12" in 10 columns '****12****'

print('{:*=10}'.format(12))
# Right-align "12" in 10 columns, sign first '********12'
print('{:*=10}'.format(-12))
# Right-align "-12" in 10 columns, sign first '-*******12'

# * -7----------4  Format Precision
# * -7----------4----1 Format Precision for Fixed-Point Format
print('{:.2f}'.format(12.3456789))  # '12.35'
print('{:.12f}'.format(12.3456789))  # '12.345678900000'

# * -7----------4----2 Format Precision for Floating-Point General Format
print('{:.5g}'.format(12.3456789))  # '12.346'
print('{:.10g}'.format(12.3456789))  # '12.3456789'
print('{:.15g}'.format(12.3456789))  # '12.3456789'
# * -7----------4----3 Format Precision for Strings
print('{:5.2s}'.format('abcdefghijkl'))  # 'ab '
print('{:5.4s}'.format('abcdefghijkl'))  # 'abcd '
print('{:5.5s}'.format('abcdefghijkl'))

# * -7----------5 Numeric Formatting
# * -7----------5----1 Zero Padding
print('{:5d}'.format(12))  # ' 12'
print('{:05d}'.format(12))  # '00012'
print('{:05d}'.format(-12))  # '-0012'
# * -7----------5----2 Sign Preservation
print('{:d}'.format(12))  # '12'
print('{:d}'.format(-12))  # '-12'
print('{:-d}'.format(12))  # '12'
print('{:-d}'.format(-12))  # '-12'
print('{:+d}'.format(12))  # '+12'
print('{:+d}'.format(-12))  # '-12'
print('{: d}'.format(12))  # ' 12'
print('{: d}'.format(-12))  # '-12'
# * -7----------5----3 Digit Grouping
print('{:,d}'.format(123456789))  # '123, 456, 789
# * -7----------5----4 Alternate Representation
print('{:b}'.format(12))  # '110'
print('{:#b}'.format(12))  # '0b1100'
print('{:o}'.format(12))  # '14'
print('{:#o}'.format(12))  # '0o14'
print('{:x}'.format(12))  # 'c'
print('{:#x}'.format(12))  # '0x'
print('{:X}'.format(12))  # 'C'
print('{:#X}'.format(12))  # '0X
print('{:.0f}'.format(12))  # '1'
print('{:#.0f}'.format(12))  # '12.'
print('{:g}'.format(1200000000))  # '1.2e+09'
print('{:#g}'.format(1200000000))  # '1.20000e+09'
print('{:G}'.format(1200000000))  # '1.2E+09'
print('{:#G}'.format(1200000000))  # '1.20000E+09''


####################################################################################################
# * ░░░░░░░░░░░░░░░░░░░░░░█████████░░░░░░░░░ #
# * ░░███████░░░░░░░░░░███▒▒▒▒▒▒▒▒███░░░░░░░ #
# * ░░█▒▒▒▒▒▒█░░░░░░░███▒▒▒▒▒▒▒▒▒▒▒▒▒███░░░░ #
# * ░░░█▒▒▒▒▒▒█░░░░██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░░ #  # * Complement de TP python
# * ░░░░█▒▒▒▒▒█░░░██▒▒▒▒▒██▒▒▒▒▒▒██▒▒▒▒▒███░ #  # * made by : Azer Hasnaoui
# * ░░░░░█▒▒▒█░░░█▒▒▒▒▒▒████▒▒▒▒████▒▒▒▒▒▒██ #  # * classroom : GLSI-1
# * ░░░█████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██ #  # * year : 2020-2021
# * ░░░█▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒██ #
# * ░██▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒██▒▒▒▒▒▒▒▒▒▒██▒▒▒▒██ #
# * ██▒▒▒███████████▒▒▒▒▒██▒▒▒▒▒▒▒▒██▒▒▒▒▒██ #
# * █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒████████▒▒▒▒▒▒▒██ #
# * ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░ #
# * ░█▒▒▒███████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░░░ #
# * ░██▒▒▒▒▒▒▒▒▒▒████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█░░░░░ #
# * ░░████████████░░░█████████████████░░░░░  #                                              # *  END
####################################################################################################
