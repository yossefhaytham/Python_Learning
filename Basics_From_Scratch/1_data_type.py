
# type()
# All Data in Python is Object

print(type(10))  # int => Integer
print(type(10+0j))  # complex number
print(type(100))  # int => Integer
print(type(-50))  # int => Integer

print(type(100.9))  # float => Floating Point Number
print(type(1.950950))  # float => Floating Point Number
print(type(-100.9595))  # float => Floating Point Number

print(type("Hello Python"))  # str => String

print(type([1, 2, 3, 4, 5]))  # list => List

print(type((1, 2, 3, 4, 5)))  # tuple => Tuple

print(type({"One": 1, "Two": 2, "Three": 3}))  # dict => Dictionary

print(type(2 == 2))  # bool => Boolean
#Any non-zero numeric value is True and zero value is False.

# -- Type Conversions --
    #data_type(expression)
x=3.14
print(int(x)) # output : 3
print(type(x)) # output : float 