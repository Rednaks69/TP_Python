#*##################################################################################################
# * Complement de TP python
# * made by : ▞▚ ▜▙ █☰ 🆁 █▬█ ▞▚ ▟▛ ▛▟ ▞▚ ██ ▙▟ █                          # ──▒▒▒▒▒▒─
# * classroom : GLSI-1                                                     # ─▒─▄▒─▄▒─
# * year : 2020-2021                                                       # ─▒▒▒▒▒▒▒─
# *##############################                                          # ─▒▒▒▒▒▒▒─
# *           -Basics-         *#                                          # ─▒─▒─▒─▒─
#*##################################################################################################
# ? Summary
# ? -1- Statement
# ? -----1-1- One Statement Per Line
# ? -----1-2- Multiple Statements Per Line
# ? -2- Quotation Marks
# ? -3- Comments
# ? -4- Basic Data Types
# ? -5- Variables
# ? -6- Basic Input and Output
######################################################################################################
#

import math
import cmath

# * -1- Statement
# * -----1-1- One Statement Per Line
print('hello world')
print("hello planet earth")
# * -----1-1- Multiple Statements Per Line
print('my name is Azer')
print("why am i \t doing this tutorial")

# * -2- Quotation Marks
# * -----2-2- single Quotes
print('"hi" from \'Mandalore\'')
# * -----2-2- Double Quotes
print("'hi' from \"Mandalore\"")
# * -----2-3- Triple Quotes
print(""" hi im from 
planet earth """)
print(""" "Mandalore" 
exist !!! """)

# * -3- Comments
# anything you write after this hash symbole (#) will be a comment
print("this is a new line")  # a comment can be in line

# * -4- Basic Data Types
# * -----4-1- Numbers
# * -----4-1----- int (integer)
print(15)
print(int(15.45))
print(int("25"))
print(int("25", 8))
# * -----4-1----- float (real)
print(12.34)
print(14e2)
print(float(15))
print(float("24"))
print(float())
# * -----4-1----- complex
print(3+2j)
print((3+2j).real)
print((3+2j).imag)

# * -----4-1-----2 Numbers Operations
# some exemple of operations
print(math.log10(100))
print(math.cos(0))
print(math.sqrt(2))
print(cmath.polar(2+3j))
print(cmath.rect(3.605551275463989, 0.982793723247329))
print(cmath.phase(3+4j))

# * -----4-2- basic string
print(str(10))
name = "grogou"
print(name[0:3])
print(name[3:])
print(name[::-1])

# \\ --->  Backslash(\)                     # ? # ──▄█▀█▄─────────██
# \' --->  Single quote (')                 # ? # ▄████████▄───▄▀█▄▄▄▄
# \" --->  Double quote (")                 # ? # ██▀▼▼▼▼▼─▄▀──█▄▄
# \a --->  Alert(beep)                      # ? # █████▄▲▲▲─▄▄▄▀───▀▄
# \b --->  Backspace                        # ? # ██████▀▀▀▀─▀────────▀▀
# \f --->  Formfeed
# \n --->  Newline
# \r --->  Carriage return t Tab
# \v --->  Vertical tab
# \ooo --->  Character with ASCII code ooo in octal
# \xhh C--->  haracter with ASCII code hh in hexadecimal
# \uhhhh --->  Unicode character with code hhhh
# \Uhhhhhhhh --->  Unicode character with code hhhhhhhh
# \N{name} --->  Unicode character with name name

# * -----4-1-----2 String Operations
# 'aBc'.lower() '
# 'aBc'.upper()
# 'hello woRLD'.capitalize()
# 'hello woRLD'.title()
# 'hello woRLD'.swapcase()
####################################################
# 'abc'.isalpha()
# 'abc'.isupper()
# 'abc'.islower()
# 'abc'.isnumeric()
# 'abc'.isalnum()
# 'abc'.isidentifier()
# 'abc'.istitle()
# 'abc'.isprintable()
# 'abc'.isspace()


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
