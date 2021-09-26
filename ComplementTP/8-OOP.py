####################################################################################################
# * Complement de TP python
# * made by : Azer Hasnaoui
# * classroom : GLSI-1
# * year : 2020-2021
####################################################################################################
#                     -OOP-                                                                        #
####################################################################################################
# ? Summary
# ? -1- Defining Classes
# ? -2- Instantiating Classes
# ? -3- Instance Variables, Class Variables, Functions and Methods
# ? -----3-1- Instance Variables
# ? -----3-2- Instance Methods
# ? -----3-3- Class Variables
# ? -----3-4- Class Functions
# ? -----3-5- Instance Methods as special Class Functions
# ? -----3-6- Public, Private and Protected Members
# ? -----3-6-----1 Protected Members
# ? -----3-6-----2 Private Members
# ? -4- Constructors and Destructors
# ? -----4-1- Constructors
# ? -----4-2- Destructors
# ? -5- Inheritance
# ? -----5-1- Simple Inheritance
# ? -----5-2- Private, Public and Protected Revisited
# ? -----5-3- Function Overriding
# ? -----5-4- Constructors and Destructors in Simple Inheritance
# ? -----5-5- Multiple Inheritance
# ? -----5-6- Function Overriding in Multiple Inheritance
# ? -----5-7- Constructors and Destructors in Multiple Inheritance
# ? -6-  Dynamic Polymorphism
# ? -----6-1- Abstract Methods and Classes
# ? -7- Attribute Handling, Magic Functions and Operator Overloading
# ? -----7-1- Attribute Handling
# ? -----7-1-----1 The hasattr() Function
# ? -----7-1-----2 The getattr() Function
# ? -----7-1-----3 The setattr() Function
# ? -----7-1-----4 The delattr() Function
# ? -----7-1-----5 Standard Attributes
# ? -----7-2- Magic Functions
# ? -----7-2-----1 Constructors and Destructors
# ? -----7-2-----2 Stringification
# ? -----7-3- Operator Overloading
# ? -----7-3-----1 Overloading Basic Arithmetic Operators
# ? -----7-3-----2 Overloading Unary Arithmetic Operators
# ? -----7-3-----3 Overloading Type Conversion Operators
# ? -----7-3-----4 Overloading Comparison Operators
# ? -----7-3-----5 Overloading Bitwise Operators
# ? -----7-3-----6 Overloading Assignment Operators
# ? -8- Empty Classes
# ? -----8-1- Empty Classes as Placeholders
# ? -----8-2- Empty Classes for Identification
# ? -----8-3- Empty Classes as Base Classes
# ? -----8-4- Empty Classes as Data Types
# ? -9- Programs based on OOP
# ? -----9-1- Implementation of Counter Class
# ? -----9-2- Implementation of Distance Class
####################################################################################################
# * -1- Defining Classes
"""
class className:
                statements
-> The statements within a class can be any of the following:
        1. Blank lines
        2. Comments
        3. Class variables
        4. Class functions
"""
# * -2- Instantiating Classes


class EmptyDate:
    """
    this is my first class in python
    """
    pass


print(EmptyDate.__doc__)
date = EmptyDate()
print(type(date))
print(date.__doc__)
# * -3- Instance Variables, Class Variables, Functions and Methods
# * -----3-1- Instance Variables


class Date:
    def setDate(self, d, m, y):
        self.day = d
        self.month = m
        self.year = y


d = Date()
d.setDate(12, 30, 2010)
print(d.day, '-', d.month, '-', d.year)

# * -----3-2- Instance Methods
print("\n--------------- * -----3-2- Instance Methods------------\n")

# class student:
#     def setStudent(self, name, age, id):
#         self.name = name
#         self.age = age
#         self.id = id

#     def getName(self): return self.name
#     def getAge(self): return self.age
#     def getId(self): return self.id


# student1 = student()
# student1.setStudent('toto', 23, 89634)
# print("this name is :{}, \nhe's age is :{}, \nhe's id is {}".format(
#     student1.getName(), student1.getAge(), student1.getId()))
##################################################################################
class student:
    def setStudent(self, name, age, id):
        if self.isValid(name, age, id):
            self.name = name
            self.age = age
            self.id = id
        else:
            print("incorrect Information")

    def getName(self): return self.name
    def getAge(self): return self.age
    def getId(self): return self.id

    def print(self): return print("this name is :{}, \nhe's age is :{}, \nhe's id is {}".format(
        self.getName(), self.getAge(), self.getId()))

    def isValid(self, name, age, id):
        if age < 0:
            return False
        if id > 99999:
            return False
        if type(name) != str:
            return False
        return True

    def addAge(self, ageToAdd):
        self.age += ageToAdd
        result = student()
        result.setStudent(self.name, self.age, self.id)
        return result


student1 = student()
student1.setStudent("toto", 23, 896)
student1.print()
student2 = student()
student2.setStudent("kikooo", 45, 678)
student2.addAge(34)
student2.print()
student3 = student1.addAge(55)
student3.print()

# * -----3-3- Class Variables


class A:
    x = 10


a = A()
b = A()
print(A.x)
a.x = 20
print(A.x)
# 10
print(a.x)
# 20
print(b.x)
# 10
# * -----3-4- Class Functions


class B:
    x = 100

    def increment():
        B.x = B.x+1


print(B.x)
B.increment()
print(B.x)
a = B()
b = B()
a.x
# 11
b.x
# 11
#! a.increment() TypeError: increment() takes 0 positional arguments but 1 was given

# * -----3-5- Instance Methods as special Class Functions


class C:
    def f(self):
        print("Hello")


a = C()
print(a.f())
print(C.f(a))
# * -----3-6- Public, Private and Protected Members
"""
    Python does not directly support these concepts and all members of a class are
    inherently public. Python does support a convention however, that might help support
    this but does not enforce it. Since all class members are anyway public, we will only
    concentrate on protected and private members in this section.
"""

# * -----3-6-----1 Protected Members
# section 5.2
# * -----3-6-----2 Private Members


class E:
    def set(self, x, y):
        self.x = x
        self.__y = y

    def printabe(self):
        print(f"{self.x},{self.__y}")


e = E()
e.set(2, 4)
e.printabe()
print(e.x)
#! e.y -> AttributeError: 'A' object has no attribute 'y'
#! e.__y  -> AttributeError: 'A' object has no attribute '__y'
print(e._E__y)
"""
    The private member __y is accessible outside the class with the name
    _E__y.
"""
# * -4- Constructors and Destructors

"""
    In OOP, a constructor is a member function of a class that is automatically invoked
    when an instance of that class is created in order to initialize the object to a valid
    state.
    A destructor is a member function of a class that is automatically invoked when
    an instance is destroyed in order to perform any clean-up required.
"""

# * -----4-1- Constructors

""""
    A constructor is identified in Python by it's special name: __init__.

    Note that the leading underscores do not make this instance method private as the method name
    does not end with at most 1 underscore – it in fact ends with 2 underscores!
"""


class employ:
    def __init__(self):
        print("constractor called ")


emp = employ()


# * -----4-2- Destructors
"""
    A destructor is an instance method that is automatically invoked when an
    object is going to be destroyed and eliminated and permits the programmer to perform
    any desired clean-up.

    A destructor is identified in Python by it's special name: __del__.
"""


class sayonara:
    def __del__(self):
        print("destructor called")


sayo = sayonara()
del sayo


class sayonarou:
    def __del__(self):
        print("destructor called for sayonarou ")


sayo1 = sayonarou()
sayo2 = sayo1    # This reference is copied from sayo1 to sayo2, ending up with 2 references to the object. Therefore, the reference count of the object becomes 2
del sayo1
del sayo2
"""
    When we delete the variable sayo1, we also decrement the reference count of the
    object referred to by a by 1. Therefore, the reference count of the object
    decrements to 1. Since it has not reached 0, the object continues to exist
    unaffected by the deletion of the variable sayo1.

    When we delete the variable sayo2, we also decrement the reference count of the
    object referred to by b by 1. The reference count now reaches 0. This is when
    the object will be destroyed, and just prior to that the destructor gets
    automatically called.
"""
# * -5- Inheritance

"""
    Inheritance is the mechanism wherein a class acquires all the features and properties
    of another class (or classes).
"""
# * -----5-1- Simple Inheritance
"""
    class derived_class(base_class):
        class_definition
"""


class one:
    pass


class derived_from_one(one):
    pass


one = one()
two = derived_from_one()
print(type(one))
print(type(two))
"""
    The class definitions are empty, but as Python requires at least 1 line in the
    definition, we have used the pass statement.
    2. The class B derives from class A: class B(A)
"""
# * -----5-2- Private, Public and Protected Revisited


class M:
    def __f1(self): print(M.f1)
    def f2(self): print(M.f2)
    def _f3(self): print(M.f3)


class N(M):
    def __g1(self): print(N.g1)
    def g2(self): print(N.g2)
    def _g3(self): print(N.g3)


n = N()
# print(n.__f1)
# print(n.__g1)
print(n.f2)
print(n.g2)
print(n._f3)
print(n._g3)


# * -----5-3- Function Overriding


class AE():
    def f(self): print("AE.f")


class BE(AE):
    def f(self):
        print("BE.f")
        # AE.f(self)
        super().f()  # invoke AE's f as part of functionality of BE


ae = AE()
be = BE()
# ae.f()
# print(AE.f())
be.f()

BE().f()
# its equale to be.f()
# its equale to BE.f(self [with self take any argument in this exemple])
#!
AE().f()
# its equale to ae.f()
# its equale to AE.f(self [with self take any argument in this exemple])

"""
    The statement AE.f(self) is very similar to the statement self.f(), with
    self referring to an instance of A. But in our case, self is referring to an
    instance of B and self.f() will result in a call to B.f(self) instead!
    
    The statement super().f() is equivalent to the statement self.f() with
    self referring to an instance of A that is housed within an instance of B that is
    currently referred to by self
"""
# * -----5-4- Constructors and Destructors in Simple Inheritance


# class AF:
#     def __init__(self):
#         print(" AF constructed")

#     def __del__(self):
#         print(" AF destroyed")


# class BF(AF):
#     def __init__(self):
#         print(" BF constructed")

#     def __del__(self):
#         print(" BF destroyed")


# bf = BF()
"""
    We observe that when we instantiate class BF, class BF's constructor is invoked,
    but class AF's constructor is not automatically invoked.
    
    Similarly, when we destroy the instance of class BF, the destructor of class BF is
    invoked, but the destructor of class AF is not automatically invoked.

    We would want the constructors of both classes to be invoked during
    construction and the destructors to be similarly automatically invoked upon
    destruction. Since this is not automatically performed by Python
"""


class AF:
    def __init__(self):
        print(" AF constructed")

    def __del__(self):
        print(" AF destroyed")


class BF(AF):
    def __init__(self):
        super().__init__()
        print(" BF constructed")

    def __del__(self):
        print(" BF destroyed")
        super().__del__()


bf = BF()
del bf

# * -----5-5- Multiple Inheritance
# multiple inheritance = class inherite from multiptles classes

"""
    jjkjlkclass className(baseClass1,baseClass2[,baseClass3...])
"""


class AA:
    def fa(self): print("fa")


class BA:
    def fb(self): print("fb")


class CAB(AA, BA):
    def fcab(self):
        super().fa()
        self.fb()    # the same as the last line but can ake some problem when it's a overriding function
        print("fcab")


c = CAB()
c.fcab()


# * -----5-6- Function Overriding in Multiple Inheritance

class AB:
    def f(self): print("a")


class BB:
    def f(self): print("b")


class CAB(AB, BB):
    def f(self):
        super().f()   # it will take alwais the bigger in the inheritance's order -> the order of inheritance is from left to right
        # self.f()    # the same as the last line but can ake some problem when it's a overriding function
        BB.f(self)
        print("fc")


c = CAB()
c.f()

# * -----5-7- Constructors and Destructors in Multiple Inheritance


class AC:
    def __init__(self): print("A constructed")
    def __del__(self): print("A destroyed")


class BC:
    def __init__(self): print("B constructed")
    def __del__(self): print("B destroyed")


class ABC(AC, BC):
    def __init__(self):
        AC.__init__(self)
        BC.__init__(self)
        print("C constructed")

    def __del__(self):
        AC.__del__(self)
        BC.__del__(self)
        print("C destroyed")


abc = ABC()
del abc
# * -6-  Dynamic Polymorphism


class Animal:
    def __init__(self, name): self.name = name
    def speak(self): print("this animal speak like :", end=" ")


class dog(Animal):
    def __init__(self):
        super().__init__("dog")

    def speak(self):
        super().speak()
        print("hab hab")


class cat(Animal):
    def __init__(self):
        super().__init__("cat")

    def speak(self):
        super().speak()
        print(" mehow mehow")


def introduce(animal):
    print("Hi the name of this animal is", animal.name)

    animal.speak()


animal1 = dog()
introduce(animal1)
animal2 = cat()
introduce(animal2)

# * -----6-1- Abstract Methods and Classes
# we will return complite this section
"""
    The class can be made an abstract class using the abc package and the method can be made 
    an abstract method using @abstractmethod.
"""

# * -7- Attribute Handling, Magic Functions and Operator Overloading
# * -----7-1- Attribute Handling
# * -----7-1-----1 The hasattr() Function
"""
    The hasattr() function tells whether a particular instance has a particular attribute
    or not.
    
    Syntax: hasattr(object,attribute)
"""


class X1:
    def __init__(self):
        self.x = 0


x1 = X1()
print(hasattr(x1, "x"))
print(hasattr(x1, "y"))


# * s-----7-1-----2 The getattr() Function
"""
    The getattr() function returns the value of an attribute within an instance if it
    exists, returning a default value (if provided) if the attribute does not exist.
    
    Syntax: getattr(object,attribute[,default])
"""


class X2:
    def __init__(self):
        self.x = 0


x2 = X2()
print(getattr(x2, "x", 2))
print(getattr(x2, "y", 2))
print(getattr(x2, "x"))
# print(getattr(x2, "y"))  # If the attribute attribute does not exist in the instance
# object and no default is provided, an AttributeError occurs.


# * -----7-1-----3 The setattr() Function
"""
    The setattr() function sets the value of an attribute in an instance. If the attribute
    already existed in the instance, it's value is overwritten and if it did not exist, it is
    created.
    
    Syntax:  setattr(object,attribute,value)
"""


class X3:
    def __init__(self):
        self.x = 0


x3 = X3()
setattr(x3, "x", 22)
setattr(x3, "y", 34)
print(getattr(x3, "x", "error"))
print(getattr(x3, "y", "error")
      )
# * -----7-1-----4 The delattr() Function
"""
    to remove an existing attribute from an instance, the delattr() function can
    be used.

    Syntax:  delattr(object,attribute)
"""


class X4:
    def __init__(self):
        self.x = 0


x4 = X4()
delattr(x4, "x")
print(hasattr(x4, "x"))

# * -----7-1-----5 Standard Attributes
"""
    __name__        The name of the class
    __doc__         The documentation string of the class
    __bases__       A tuple containing the base classes of this class, in the order of inheritance
    __module__      The name of the module to which this class belongs
    __dict__        A dictionary containing the namespace of this class
"""


class a100:
    pass


class b100:
    pass


class c100(a100, b100):
    "Class desmostration of attributes"
    x100 = 0
    def __init__(self): pass
    def fc100(self): pass


print("__name__:", c100.__name__)
print("__doc__:", c100.__doc__)
print("__bases__:", c100.__bases__)
print("__module__:", c100.__module__)
print("__dict__:", c100.__dict__)


# * -----7-2- Magic Functions
"""
    We use the term “Magic Functions” to denote those functions/methods that are
    automatically invoked without us explicitly naming them! All of these magic functions
    have the speciality that they have the following 

    syntax for their name:  __name__
"""
# * -----7-2-----1 Constructors and Destructors


class A101:
    def __init__(self): print("Created")
    def __del__(self): print("Destroyed")


a101 = A101()
del(a101)


# * -----7-2-----2 Stringification
"""
    We use the term “stringification” to describe the conversion of an object to a string, and we use the
    following syntax to perform stringification: str(object)
"""


class A102:
    pass


a102 = A102()
print(str(a102))


class A103:
    def __str__(self): return "hi from __str__ function"


a103 = A103()
print(str(a103))

# * -----7-3- Operator Overloading
# * -----7-3-----1 Overloading Basic Arithmetic Operators
# * -----7-3-----2 Overloading Unary Arithmetic Operators
# * -----7-3-----3 Overloading Type Conversion Operators
# * -----7-3-----4 Overloading Comparison Operators
# * -----7-3-----5 Overloading Bitwise Operators
# * -----7-3-----6 Overloading Assignment Operators
# ? -8- Empty Classes
# ? -----8-1- Empty Classes as Placeholders
# ? -----8-2- Empty Classes for Identification
# ? -----8-3- Empty Classes as Base Classes
# ? -----8-4- Empty Classes as Data Types
# ? -9- Programs based on OOP
# ! -----9-2- Implementation of Distance Class
# ! -----9-1- Implementation of Counter Class
