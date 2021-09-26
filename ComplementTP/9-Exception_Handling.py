####################################################################################################
# * Complement de TP python
# * made by : Azer Hasnaoui
# * classroom : GLSI-1
# * year : 2020-2021
####################################################################################################
#                     -Exception_Handling-                                                         #
####################################################################################################
# ? Summary
# ? -1- Handling Exceptions
# ? -----1-1- The Basic Exception Handling Block
# ? -----1-2- Handling Multiple Exceptions
# ? -----1-2-----1 Separate Handling of Each Exception
# ? -----1-2-----2 Common Handling of Multiple Exceptions
# ? -----1-2-----3 Handling All Exceptions
# ? -----1-3- Dealing with Exception Instances
# ? -----1-4- The else Clause
# ? -----1-5- The finally Clause
# ? -2- Raising Exceptions
# ? -3- Exception Propagation
# ? -----3-1- Exception Propagation Through Nested Blocks
# ? -----3-2- Exception Propagation Through Functions
# ? -4- Re-Raising Exceptions
# ? -5- User-Defined Exceptions
####################################################################################################
# * -1- Handling Exceptions
# * -----1-1- The Basic Exception Handling Block
"""
Syntax:

    try:
    ...
    except exceptionName:
    ...

"""
try:
    n = int(input("enter an integer : "))
    quotient = int(100/n)
    print(f"100/{n}={quotient}")
except ZeroDivisionError:
    print("Division by zero is impossible")


# * -----1-2- Handling Multiple Exceptions
# * -----1-2-----1 Separate Handling of Each Exception
"""
Syntax:

        try:
            # try block
        except ExceptionName1:
            # Exception handler for ExceptionName1
        except ExceptionName2:
            # Exception handler for ExceptionName2
        except ExceptionName3:
            # Exception handler for ExceptionName3
        ...
"""
try:
    n = int(input("Enter a positif number: "))
    quotient = 100/n
    print(f"the quotient of 100/{n} is: {quotient}")
except ValueError:
    print("error value incorrect")
except ZeroDivisionError:
    print("the division by zero is impossible")

# * -----1-2-----2 Common Handling of Multiple Exceptions
"""
Syntax:
        try:
        ... # try block
        except (ExceptionName1, ExceptionName2 [,ExceptionName3...]):
        ... # except block

"""
try:
    n = int(input("Enter a positif number: "))
    quotient = 100 / n
    print(f"100/{n} is {quotient}")
except(ZeroDivisionError, ValueError):
    print("Into Exception ")

"""
Syntax:
    try:
    ... # try block
    except ExceptionName1:
    ... # except block
    except (ExceptionName2, ExceptionName3, ExceptionName4):
    ... # except block
    except (ExceptionName5, exceptionName6):
    ... # except block
    except ExceptionName7:
    ... # except block
"""
try:
    n = int(input("Enter a positif number: "))
    quotient = 100 / n
    print(f"100/{n} is {quotient}")
except(ZeroDivisionError, ValueError):
    print("Into Exception ")
except ReferenceError:
    print("reference error")

# * -----1-2-----3 Handling All Exceptions
"""
    try:
    ... # try block
    except ExceptionName1:
    ... # Single exception handler
    except (ExceptionName2, ExceptionName3):
    ... # Multiple exception handler
    except:
    ... # Handles all exceptions not handled above
"""
try:
    n = int(input("Enter a positif number: "))
    quotient = 100 / n
    print(f"100/{n} is {quotient}")
except:
    print("OoOopzzz")

# * -----1-3- Dealing with Exception Instances
"""
syntax:

    try:
    ...  # try block
    except ExceptionName1 as e:
    ...  # Handler ExceptionName1 with instance as e
    except (ExceptionName2, ExceptionName3) as e:
    ...  # Handle both these exceptions with instance as e

"""
try:
    n = int(input("Enter a positif number: "))
    quotient = 100 / n
    print(f"100/{n} is {quotient}")
except Exception as e:
    print("Oopzzz")
#     print("details of exception: ", e)

# # * -----1-4- The else Clause
"""
Syntax:

    try:
    ... # try block, monitored for exceptions
    except:
    ... # except block, to respond to exceptions
    else:
    ... # else block, not monitored for exceptions

"""
try:
    n = int(input("Enter a positif number: "))
    quotient = 100 / n
except Exception as e:
    print("Oopzzz")
    print("details of exception: ", e)
else:
    print(f"100/{n} is {quotient}")

# * -----1-5- The finally Clause
"""
Syntax:

    try:
    ... # try block
    except:
    ... # except block
    else:
    ... # else block
    finally:
    ... # finally block

"""
try:
    n = int(input("Enter a positif number: "))
    quotient = 100 / n
except:
    print("Oopzzz")
    # print("details of exception: ", e)
else:
    print(f"100/{n} is {quotient}")
finally:
    print("this program is done !")

# * -2- Raising Exceptions
"""
Syntax :
    raise exceptionInstance
"""
try:
    n = int(input("Enter a positif number: "))
    if n > 100:
        raise ValueError
    quotient = 100 / n
except ValueError:
    print("number have to be less than 100")
except ZeroDivisionError:
    print("number zero can't be divided")
    # print("details of exception: ", e)
except Exception as e:
    print("details: ", e)
else:
    print(f"100/{n} is {quotient}")
finally:
    print("program done !")

# * -3- Exception Propagation
# * -----3-1- Exception Propagation Through Nested Blocks
try:
    try:
        n = int(input("Enter an integer "))
        quotient = int(100 / n)
        print(f"100/{n}= {quotient}")
    except ValueError:
        print("Enter a correct value ")
except ValueError:
    print("invalid value !")
except ZeroDivisionError:
    print("0 can't be divided")

# * -----3-2- Exception Propagation Through Functions


def greeting():
    try:
        name = str(input("try to put ur name: "))
        print(f"welocome {name}")
    except:
        print("hey punk, this is not a name, next time try harder")


def asking_for_age():
    try:
        age = int(input("put ur age : "))
        if(age > 120):
            raise ValueError
        if(age <= 0):
            raise ZeroDivisionError
    except ValueError:
        print("this person is dead and burry ")
    except ZeroDivisionError:
        print("Are u dumb age can't be a negatif number ")
    else:
        print(f"ur age is {age}")


try:
    greeting()
    asking_for_age()
except:
    print("something is not working")
finally:
    print("importants things")

# * -4- Re-Raising Exceptions
"""
    def f():
        try:
        ... # try block
        except ExceptionName:
        ... # Handle the exception
        raise # Report to caller that this exception occurred
    try:
    f() # Call the function f
    ... # Do other stuff if the call to f() was exception-free
    except ExceptionName:
    ... # Respond to the exception

"""
"""
     This syntax is understood to mean that we wish to raise the same exception that we are currently handling.
     
     This special syntax of raise is only available within the except block, and ends up raising the same exception object
     that we are currently handling.
"""
# * -5- User-Defined Exceptions

# * -5-1


class DEADPERSON(Exception):
    def __str__(self): print("HI!")


def greeting():
    try:
        name = str(input("try to put ur name: "))
        print(f"welocome {name}")
    except:
        print("hey punk, this is not a name, next time try harder")


def asking_for_age():
    try:
        age = int(input("put ur age : "))
        if(age > 120):
            raise DEADPERSON
        if(age <= 0):
            raise ZeroDivisionError
    except DEADPERSON as e:
        print("this person is dead and burry ")
        print(e.__str__)
    except ZeroDivisionError:
        print("Are u dumb age can't be a negatif number ")
    else:
        print(f"ur age is {age}")


try:
    greeting()
    asking_for_age()
except:
    print("something is not working")
finally:
    print("importens things")

# * -5-2


class DEADPERSON(Exception):
    def __init__(self, value): self._value = value
    def getValue(self): return self._value
    def __str__(self): print("HI!")


def greeting():
    try:
        name = str(input("try to put ur name: "))
        print(f"welocome {name}")
    except:
        print("hey punk, this is not a name, next time try harder")


def asking_for_age():
    try:
        age = int(input("put ur age : "))
        if(age > 120):
            raise DEADPERSON(age)
        if(age <= 0):
            raise ZeroDivisionError
    except DEADPERSON as e:
        print(
            f"you put an age of {e.getValue()}, this person must be dead and burry ")
        print(e.__str__())
    except ZeroDivisionError:
        print("Are u dumb age can't be a negatif number ")
    else:
        print(f"ur age is {age}")


try:
    greeting()
    asking_for_age()
except:
    print("something is not working")
finally:
    print("importens things")

# * -5-3

"""
    As a final example, let us create exception classes that do not inherit from
    Exception directly, but indirectly derive from it by deriving directly from one of it's
    derived classes instead. Let us design our OverflowException and
    NegativeInputException classes to derive from ValueError instead of
    Exception.
"""


class OverflowException(ValueError):
    pass


class NegativeInputException(ValueError):
    pass


def check(n):
    if n > 100:
        raise OverflowException()
    if n < 0:
        raise NegativeInputException()


try:
    n = int(input("Enter an integer:"))
    check(n)
    quotient = int(100/n)
    print("100/{} = {}".format(n, quotient))
except ValueError:
    print("Please enter an integer between 0 and 100!")
except ZeroDivisionError:
    print("Sorry! Division by zero is not permitted!")


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
