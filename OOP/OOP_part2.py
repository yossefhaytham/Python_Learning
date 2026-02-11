# ======================================================
# Evolution of Programming Data Models
# ======================================================
# ------------------------------------------------------
# 1) Primitive Data Types
# ------------------------------------------------------
# - Basic types like int, float, char, and bool.
# - Each value stands alone with no logical connection.
# - Functions operate on data separately.
# - Hard to manage when multiple related data pieces are needed.
# Reason to move on:
# → Need a way to group related data elements together.

# ------------------------------------------------------
# 2) Structs (Structured Data)
# ------------------------------------------------------
# - Introduced to combine multiple data fields into one unit.
# - Groups of fixed number of components , accessed by name.
# - member may be of different types.
# - Example (in C):
#       struct Student {
#           string fname;
#           string lname;
#           int age;
#           float grade;
#       };
#      Student s1;  // create a struct variable
#     s1.fname = "Youssef";  // access members ......
# - Now data is grouped logically.
# - But the problem: functions that work on these structs are still defined outside the struct.
# - Data and behavior remain separate.
# Reason to move on:
# → Need a system where data and its behavior are packaged together.

# ------------------------------------------------------
# 3) Object-Oriented Programming (OOP)
# ------------------------------------------------------
# - Combines both data (attributes) and behavior (methods) in a single unit called a "class".
# - Each instance (object) has its own data and can perform actions using its methods.
# - Encourages code reuse, organization, and scalability.
# Key difference from structs:
# - Structs only store data.
# - OOP classes store data + functions that operate on that data.
# ======================================================
# Inheritance 
# ======================================================

# Inheritance means a child class can use attributes and methods
#   from a parent class (code reuse + organization)
class Parent:
    def __init__(self, parent_name):
        self.parent_name = parent_name
        print("Parent constructor called")

    def show_name(self):
        print(f"Parent Name: {self.parent_name}")

class Child(Parent):
    def __init__(self, parent_name, child_name, age):
        # call parent constructor to initialize parent info
        super().__init__(parent_name)
        self.child_name = child_name
        self.age = age
        print("Child constructor called")

    def show_info(self):
        print(f"Child: {self.child_name}, Age: {self.age}, Parent: {self.parent_name}")

child1 = Child("Ahmed", "Youssef", 21)
child1.show_name()   # method from parent
child1.show_info()   # method from child
# ------------------------------------------------------
# super() function
# ------------------------------------------------------
# used to call parent class methods (especially constructors)
class Vehicle:
    def __init__(self, brand):
        self.brand = brand
        print("Vehicle constructor called")

    def show_info(self):
        print(f"Vehicle Brand: {self.brand}")

class Car(Vehicle):
    def __init__(self, brand, model):
        # call parent constructor using super()
        super().__init__(brand)
        self.model = model
        print("Car constructor called")

    def show_info(self):
        # extend parent behavior
        super().show_info()
        print(f"Model: {self.model}")

car1 = Car("Toyota", "Corolla")
car1.show_info()
# ------------------------------------------------------
# Types of Inheritance
# ------------------------------------------------------
# Single Inheritance → one parent, one child
class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greet_child(self):
        print("Hello from Child")

c = Child()
c.greet()
c.greet_child()


# Multilevel Inheritance → chain of inheritance
class GrandParent:
    def message(self):
        print("Message from GrandParent")

class Parent(GrandParent):
    pass

class Child(Parent):
    pass

obj = Child()
obj.message()  # inherited from GrandParent

# Multiple Inheritance → child inherits from multiple parents
class Father:
    def skills(self):
        print("Father: Driving, Teaching")
class Mother:
    def skills(self):
        print("Mother: Cooking, Dancing")
class Son(Father, Mother):
    def skills(self):
        # super() will follow MRO (method resolution order)
        super().skills()
        print("Son: Coding, Gaming")
s = Son()
s.skills()
print(Son.__mro__)  # shows order of inheritance lookup

# Hierarchical Inheritance → multiple children share one parent
class Animal:
    def sound(self):
        print("Animal makes a sound")

class Cat(Animal):
    def sound(self):
        print("Meow")

class Cow(Animal):
    def sound(self):
        print("Moo")
cat = Cat()
cow = Cow()
cat.sound()
cow.sound()
# Hybrid Inheritance → mix of multiple types
# (supported in Python, but can become complex due to MRO rules)
# ------------------------------------------------------
# Helper functions
# ------------------------------------------------------
# isinstance() → check if object is instance of a class
# issubclass() → check if class is subclass of another

print(isinstance(cat, Animal))  # True
print(issubclass(Cat, Animal))  # True
#=======================================================
# Encapsulation 
#========================================================
# Encapsulation means restricting direct access to some data (attributes)
# and allowing controlled access through methods (getters & setters).
# This helps protect the data from being changed accidentally from outside the class.

# Access Modifiers in Python:
# 1. Public:   variable_name
#    - Can be accessed and modified freely from anywhere.
# 2. Protected: _variable_name
#    - Should be accessed only inside the class and its subclasses.
#      (This is only a convention, Python won't stop you from accessing it.)
# 3. Private: __variable_name
# NOTE- Name mangling makes it harder to access from outside   but still possible by ==>(ClassName.__variable_name),
#     So, encapsulation in Python is more of a "rule" than a strict restriction.

class Person:
    def __init__(self, name, age):
        self.name = name           # Public attribute
        self._age = age            # Protected attribute
        self.__salary = 5000       # Private attribute

    # Getter method: used to read private/protected data safely
    def get_salary(self):
        return self.__salary

    # Setter method: used to modify private/protected data safely
    def set_salary(self, new_salary):
        if new_salary > 0:
            self.__salary = new_salary
        else:
            print("Invalid salary amount!")

    # Example of showing encapsulation effect
    def show_info(self):
        print(f"Name: {self.name}, Age: {self._age}, Salary: {self.__salary}")

# Creating an object
person1 = Person("Youssef", 21)

# Accessing public variable directly
print(person1.name)  # Allowed

# Accessing protected variable (allowed but not recommended)
print(person1._age)

# Accessing private variable directly will cause an error:
# print(person1.__salary)  # AttributeError

# Correct way: use getter and setter methods
print(person1.get_salary())  # Correct
person1.set_salary(7000)
print(person1.get_salary())

# NOTE NOTE NOTE Technically, we can still access private data using name mangling (not recommended)
print(person1._Person__salary)  # Works but breaks encapsulation rule

person1.show_info()
# ------------------------------------------------------
# 4. The Pythonic Way: Property Decorators (@property) NOTE NOTE NOTE
# ========================================================
# In Python, we don't usually use get_method() and set_method().
# Instead, we use the @property decorator to make a method behave like an attribute.
# This keeps the code clean (No parentheses needed) while maintaining control.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary  # Private attribute

    # The Getter: Accesses the value like an attribute
    @property
    def salary(self):
        """Allows you to use 'obj.salary' instead of 'obj.get_salary()'"""
        print("Accessing salary data...")
        return self.__salary

    # The Setter: Validates and sets the value using '='
    @salary.setter
    def salary(self, value):
        """Allows you to use 'obj.salary = 100' instead of 'obj.set_salary(100)'"""
        if value > 0:
            print(f"Updating salary to {value}")
            self.__salary = value
        else:
            print("Error: Salary must be positive!")

# --- Usage of Property ---
emp = Employee("Youssef", 5000)

# 1. Getter in action (No parentheses used)
print(emp.salary) 

# 2. Setter in action (Using the '=' operator)
emp.salary = 6000   # Works perfectly and runs the validation logic
emp.salary = -100   # Triggers the error message inside the setter
# ======================================================
# Abstraction 
# ======================================================

# Abstraction means hiding complex implementation details 
# and showing only the necessary features to the user.
# Example: You can drive a car (start, stop, accelerate)
# without knowing how the engine internally works.

# In Python, abstraction is achieved using Abstract Classes and Methods.
# These are provided by the 'abc' module (Abstract Base Class).

from abc import ABC, abstractmethod

# ------------------------------------------------------
# Abstract Class
# ------------------------------------------------------
# Abstraction means hiding the complex NOTE (implementation) details and showing 
# only the essential features of an object. 
# It acts as a "Contract" or "Blueprint" for other classes.

# Key Points in Python:
# 1. Abstract Class: A class that cannot be instantiated (you can't create an object from it).
# 2. Abstract Method: A method that is declared but contains no implementation NOTE (using @abstractmethod).
# 3. Any subclass inheriting from an abstract class MUST implement all its abstract methods,
#    otherwise, Python will raise a TypeError.
# 4. We use the 'abc' module (Abstract Base Classes) to achieve this.

# - An abstract class acts as a blueprint for other classes.
# - It is created only to be inherited, not instantiated directly.
# - It can define abstract methods that must be implemented 
#   in any subclass that inherits from it.
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        # abstract method (no implementation here)
        pass

    @abstractmethod
    def stop(self):
        # abstract method (no implementation here)
        pass
# ------------------------------------------------------
# Subclasses must implement all abstract methods
# ------------------------------------------------------
class Car(Vehicle):
    def start(self):
        print("Car engine started.")

    def stop(self):
        print("Car engine stopped.")

class Bike(Vehicle):
    def start(self):
        print("Bike engine started.")

    def stop(self):
        print("Bike engine stopped.")
# ------------------------------------------------------
# Example Usage
# ------------------------------------------------------
# v = Vehicle()  # NOTE ERROR: cannot create an object from abstract class

car = Car()
car.start()  # Car engine started.
car.stop()   # Car engine stopped.

bike = Bike()
bike.start()  # Bike engine started.
bike.stop()   # Bike engine stopped.

# ------------------------------------------------------
# Notes:
# ------------------------------------------------------
# - Abstraction focuses on “what to do” instead of “how to do”.
# - The abstract class defines the structure (the rules).
# - Subclasses provide the actual implementation.
# - This makes the system flexible and easier to extend.
# - Example: You can later add a Truck class that implements start() and stop() differently.

# ------------------------------------------------------
# Relation to Encapsulation:
# ------------------------------------------------------
# - Encapsulation hides the internal data (variables, methods) within a class.
# - Abstraction hides unnecessary implementation details from the user.
# Example :-
# when driving a car, the driver moves the steering wheel, 
# presses the brakes, and then the transmission without needing to know how the engine works.
# This is considered part of the abstraction inside the car.
# The components of the engine and the internal parts of the car are hidden and cannot be accessed directly. This is encapsulation.
# ======================================================
# Polymorphism 
# ======================================================
# - Polymorphism means "many forms"
# - In Python it mainly appears as:
#     1) Method Overriding → same method name in parent & child.
#     2) Method Overloading → same method name with different parameters (simulated).
# ------------------------------------------------------
# 1) Method Overriding 
# ------------------------------------------------------
class Animal:
    def speak(self):
        return "some sound"
class Dog(Animal):
    # child class overrides parent method
    def speak(self):
        return "woof"
a1 = Animal()
a2 = Dog()
print(a1.speak())   # Output: some sound
print(a2.speak())   # Output: woof  (method overridden)
# ------------------------------------------------------
# 2) Method Overloading
# ------------------------------------------------------
# Python doesn’t support true overloading. NOTE NOTE
# We simulate it using default or variable arguments.
class Math:
    def add(self, a, b=0, c=0):
        return a + b + c
m = Math()
print(m.add(3, 4))        # 7   (uses 2 arguments)
print(m.add(3, 4, 5))     # 12  (uses 3 arguments)
# ------------------------------------------------------
# Notes:
# ------------------------------------------------------
# - Overriding → redefine a parent’s method inside the child class.
# - Overloading → one method behaves differently based on arguments (manual in Python).
# ======================================================