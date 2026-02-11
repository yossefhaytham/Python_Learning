# -------------
# -- Strings --
# -------------

myStringOne = 'This is Single Quote'
myStringTwo = "This is Double Quotes"

print(myStringOne)
print(myStringTwo)
print(myStringTwo[1])# Index 1 => h
print(myStringTwo[-1])  # Index -1 => First Character From End
print(myStringTwo[-6])  # Index -6 => 6th Character From End

myStringThree = 'This is Single Quote "Test"'
myStringFour = "This is Double Quotes 'Test'"

# Slicing ( Access Multiple Sequence Items )
# [Start:End] End Not Included
# [Start:End:Steps]
myString = "I Love Python"

print(myString[:10])  # If Start Is Not Here Will Start From 0 (I Love Pyt)
print(myString[5:])  # If End Is Not Here Will Go To The End (e Python)
print(myString[:])  # Full Data

print(myString[0::1])  # Full Data
print(myString[::1])  # Full Data

print(myStringThree)
print(myStringFour)

myStringFive = '''First
Second 'Test' "Test"
Third'''

myStringSix = """First
Second "Test" \\\ 'Test'
Third"""

print(myStringFive)
print(myStringSix)
#====================================================================
# --- print() function in Python ---
# Syntax: print(expressions, sep=None, end=None)
# expressions -> the values to be printed
# sep -> separator between values (default is space " ")
# end -> what to print at the end (default is newline "\n")

# Example 1: default behavior
print("Hello", "World")  
# Output: Hello World   (sep = " ", end = "\n")

# Example 2: custom separator
print("Hello", "World", sep="-")  
# Output: Hello-World

# Example 3: custom end
print("Hello", end=" ")
print("World")  
# Output: Hello World   (on the same line because end=" ")

# Example 4: both sep and end
print("A", "B", "C", sep="*", end=" END\n")  
# Output: A*B*C END
