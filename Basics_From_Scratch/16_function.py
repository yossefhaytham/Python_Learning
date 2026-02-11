# [1] A Function is A Reusable Block Of Code Do A Task
# [2] A Function Run When You Call It
# [3] A Function Accept Element To Deal With Called [Parameters]
# [4] A Function Can Do The Task Without Returning Data
# [5] A Function Can Return Data After Job is Finished
# [6] A Function Create To Prevent DRY (donnot repeat yourself)
# [7] A Function Accept Elements When You Call It Called [Arguments]
# [8] There's A Built-In Functions and User Defined Functions
#========================================================================

# def                     => Function Keyword [Define]
# say_hello()             => Function Name
# name                    => Parameter
# print(f"Hello {name}")  => Task (block code)
# say_hello("yossef")     => yossef is The Argument

def say_hello(name):
    print(f"Hello {name}")

say_hello("yossef")

# -----------------------------------------------------------------------

# This function uses *args to accept a variable number of positional arguments.
# *args packs all extra arguments into a tuple → this is called "packing".
def sum_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

# Example usage with direct values (3, 5, 7) → packed into *args as a tuple
print(sum_numbers(3, 5, 7))  # Output: 15

# You can also use a list and unpack it using * before passing
# This is called "unpacking" – the list elements are sent as separate arguments
numbers = [4, 6, 10]
print(sum_numbers(*numbers))  # Output: 20

#=======================================================================================#

# You can assign a default value to a parameter by using "=" in the function definition.
# Example: def greet(name="Guest"): → if no name is passed, "Guest" will be used.
def greet(name="Guest"):
    print(f"Hello, {name}!")

# Default value is used because no argument is passed
greet()  # Output: Hello, Guest!

# If an argument is passed, it overrides the default
greet("Youssef")  # Output: Hello, Youssef

# IMPORTANT:
# If you use a default value in one parameter,
# make sure all parameters **after it** also have default values.
# You can't put a default parameter before a required one — that causes a SyntaxError.

# This will raise an error:
# def wrong_example(name="Guest", age):  → Error

# Correct order:
def correct_example(age, name="Guest"):
    print(f"{name} is {age} years old.")

# -----------------------------------------------------------------------

# 1. Using *args in function parameters
# *args means: collect any extra positional arguments into a tuple
def show_args(*args):
    print("Args:", args)
    print("Type of args:", type(args))  # <class 'tuple'>

show_args(1, 2, 3)
# Output: Args: (1, 2, 3)

# -----------------------------------------------------------------------

# 2. Using **kwargs in function parameters
# **kwargs means: collect any extra keyword arguments into a dictionary
def show_kwargs(**kwargs):
    print("Kwargs:", kwargs)
    print("Type of kwargs:", type(kwargs))  # <class 'dict'>

show_kwargs(name="Youssef", age=20)
# Output: Kwargs: {'name': 'Youssef', 'age': 20}

# -----------------------------------------------------------------------

# 3. Using * in arguments (unpacking a list/tuple)
# * in call means: unpack the values and pass them as individual arguments
def greet(name, age):
    print(f"{name} is {age} years old.")

data = ["Youssef", 20]
print("Type of data:", type(data))  # <class 'list'>
greet(*data)
# Same as: greet("Youssef", 20)

# -----------------------------------------------------------------------

# 4. Using ** in arguments (unpacking a dictionary)
# ** in call means: unpack the dictionary into keyword arguments
info = {"name": "Youssef", "age": 20}
print("Type of info:", type(info))  # <class 'dict'>
greet(**info)
# Same as: greet(name="Youssef", age=20)

# -----------------------------------------------------------------------

# 5. Important note: order of parameters in function definition
# If you use default values, they must come AFTER required parameters
#  Wrong:
# def func(name="Guest", age): → SyntaxError

#  Correct:
def correct_func(age, name="Guest"):
    print(f"{name} is {age} years old.")
