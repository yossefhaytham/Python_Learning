# ======================================================
# Object-Oriented Programming (OOP)
# ======================================================

# Python is a multi-paradigm language — it supports:
# 1. Procedural Programming
# 2. Object-Oriented Programming (OOP)
# 3. Functional Programming
#
# OOP is a programming style that helps organize code 
# into objects, making it modular, reusable, and readable.
# In OOP, we group:
#   - Attributes (Data / Properties)
#   - Methods (Behaviors / Functions)
# NOTE Everything in Python is an Object.
# ------------------------------------------------------
# CLASS
# ------------------------------------------------------
# A class is a blueprint or template used to create objects.
# It defines the attributes (variables) and methods (functions)
# that the objects created from it will have.

# ----------------------------
# Syntax of a Class
# ----------------------------
# class ClassName:
#     def __init__(self, parameters): 
#         # constructor code (initialize attributes)
#     def method_name(self):
#         # method code

# ------------------------------------------------------
# CONSTRUCTOR (__init__)
# ------------------------------------------------------
# - The constructor is a special method called automatically
#   whenever an object is created from the class.
# - It runs once per object creation.
# - Used to initialize object attributes.
# - The first parameter is always `self`, which refers to 
#   the current object (the one being created or used).

# Example:
class Student:
    def __init__(self, name, age):
        # `self` represents the current object instance
        # These are instance attributes → unique per object
        self.name = name
        self.age = age
        print("A new Student object has been created!")

    def show_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

# ------------------------------------------------------
# Creating Objects (Instances)
# ------------------------------------------------------
# When we create an object, the constructor __init__() runs once automatically.
# Each object has its own copy of attributes.

student1 = Student("Youssef", 21)   # constructor called
student2 = Student("Sara", 22)      # constructor called again

# ------------------------------------------------------
# Accessing Attributes and Methods
# ------------------------------------------------------
# Syntax:
# object_name.attribute
# object_name.method()

print(student1.name)    # Access attribute → Output: Youssef
student1.show_info()    # Call method     → Output: Name: Youssef, Age: 21

print(student2.age)     # Access attribute → Output: 22
student2.show_info()    # Call method     → Output: Name: Sara, Age: 22

# ------------------------------------------------------
# Notes:
# ------------------------------------------------------
# - The `self` keyword ensures that attributes and methods belong
#   to the specific object instance.
# - Each time you create a new object, __init__() is called once.
# - Without `self`, Python wouldn’t know which object’s data to use.
# - A class is just a blueprint — the object is the actual instance in memory.
# - Any function defined inside a class as instance method must include `self` as its first parameter.

# ======================================================
# Python Class Methods Types
# ======================================================

# ------------------------------------------------------
# 1) Instance Method
# ------------------------------------------------------
# - Defined normally with 'self' as the first parameter.
# - Runs each time you create and use an object.
# - 'self' refers to the current object (shows ownership).
# - Used to assign or modify instance attributes.

class School:
    school_name = "Sunrise High School"  # class-level attribute

    def __init__(self, student_name, grade):
        # Instance Method → 1- used for assigning attributes
        self.student_name = student_name
        self.grade = grade
        print(f"New student {self.student_name} registered.")  # instance method runs for each object

    def show_info(self):
        # Instance Method → 2- accessing object-specific data
        print(f"{self.student_name} studies at {self.school_name} with grade {self.grade}")

# ------------------------------------------------------
# 2) Class Method
# ------------------------------------------------------
# - Decorated with @classmethod before method.
# - First parameter is 'cls', NOTE referring to the class itself.
# - Used to modify class-level data NOTE (shared by all instances).
# - Can also work as an alternative constructor.
# - Called as: ClassName.method_name(args)
# - To called class attributes in this method : cls.attributes_name

    @classmethod
    def change_school(cls, new_name):
        cls.school_name = new_name
        print(f"School name changed to {cls.school_name}")

# ------------------------------------------------------
# 3) Static Method
# ------------------------------------------------------
# - Decorated with @staticmethod before method.
# - No 'self' or 'cls' needed.
# - Used for general-purpose or logical utility tasks
#   related to the class but not dependent on its data.
# Static method cannot access class variables directly because it has no 'cls' or 'self'.
# It should not depend on class state; it is used only for helper logic.
# Class variables can still be accessed explicitly using the class name (ClassName.variable).

    @staticmethod
    def is_valid_grade(grade):
        # Static Method → performs a check not using class/instance data
        valid_grades = ["A", "B", "C", "D", "F"]
        return grade in valid_grades


# ======================================================
# Example Usage
# ======================================================

# Create student objects → triggers instance methods
s1 = School("Ali", "A")
s2 = School("Mona", "B")

# Instance method → works with object-specific data
s1.show_info()
s2.show_info()

# Class method → changes shared class-level data
School.change_school("Future Academy")
s1.show_info()  # both objects reflect new school name
s2.show_info()

# Static method → general logic unrelated to class data
print(School.is_valid_grade("A"))  # True
print(School.is_valid_grade("Z"))  # False  (invalid)

# ------------------------------------------------------
# Notes:
# Instance Method:
#   - Uses 'self' → belongs to an individual object.
#   - Can read/modify instance + class data.
#
# Class Method:
#   - Uses 'cls' → belongs to the class itself.
#   - Can modify class-level data (shared by all instances).
#   - Can act as an alternative constructor.
#                   Alternative constructor:
#    Creates a new object using classmethod instead of __init__.
#    Useful when data comes in a different format (e.g., a single string).

# Static Method:
#   - No 'self' or 'cls'.
#   - Used for general helper logic linked to the class conceptually.
# NOTE NOTE NOTE:
# Validation → Static Method
# Factory / Configuration → Class Method
# User actions → Instance Method
# ======================================================
# Dunder (Magic) Methods Example
# ======================================================

# Dunder methods allow classes to behave like built-in types.
# Here we'll use: __init__, __str__, __len__, and __mro__
class Person:
    def __init__(self, name):
        # __init__ runs automatically when an object is created
        self.name = name
        print("Person constructor called")

    def __str__(self):
        # __str__ defines what appears when we print the object
        return f"Person Name: {self.name}"

    def __len__(self):
        # __len__ makes len(object) work → here we return the name length
        return len(self.name)
# create object to show __mro__
class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade
        print("Student constructor called")

s1 = Student("Youssef", "A")

# __str__ is called automatically when using print()
print(s1)   # Output: Person Name: Youssef

# __len__ is used when calling len()
print(len(s1))  # Output: 7  (length of "Youssef")

# __mro__ shows the inheritance search order
print(Student.__mro__)
# Output: (<class '__main__.Student'>, <class '__main__.Person'>, <class 'object'>)