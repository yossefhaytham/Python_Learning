# ========================================================================================= #
# -----------------------------
# Conditional Statements (if / elif / else)
# -----------------------------
# if condition:
#     block of code
# elif another_condition:
#     block of code
# else:
#     block of code if all above conditions are False
# or
# ternary conditional operator 
# if condition true | if condition | else if condition false

x = 10
if x > 15:
    print("Greater than 15")
elif x > 5:
    print("Greater than 5 but less than or equal to 15")
else:
    print("5 or less")
# Output: Greater than 5 but less than or equal to 15

MyList = ["Yossef", "Yassin", "Fathy"]
print("exist" if "Yossef" in MyList else "not exist")  # output : exist
# ========================================================================================= #
# -----------------------------
# match-case Statement
# -----------------------------
# Introduced in Python 3.10
# Similar to "switch" in other languages.
# match variable:
#     case value1:
#         block of code
#     case value2:
#         block of code
#     case _:
#         default block (if nothing matches)

day = "Monday"

match day:
    case "Monday":
        print("Start of the week")
    case "Friday":
        print("Weekend is near")
    case _:
        print("Regular day")
# Output: Start of the week

# Key Differences Between match-case in Python and switch in other languages:
# 1. Python uses "match" instead of "switch".
# 2. Each "case" is checked against the value of the variable in match.
# 3. The underscore "_" is used as a default case (like "default" in switch).
# 4. match-case is more powerful because it supports pattern matching,
#    not just simple value comparison (can match structures, types, etc.).

# Example: Matching by type
value = [1, 2, 3]

match value:
    case int():
        print("It's an integer")
    case list():
        print("It's a list")
    case _:
        print("Unknown type")
# Output: It's a list

# ========================================================================================= #
# -----------------------------
# Loop => For
# -----------------------------
# for item in iterable_object:
#     Do something with item

for number in range(1, 6):
    print(number, end=" ")  # Output: 1 2 3 4 5
print()

# Dictionary Example
skills = {"Python": "90%", "HTML": "80%", "CSS": "70%"}
for skill in skills:
    print(skill, "=>", skills[skill])
# Output:
# Python => 90%
# HTML => 80%
# CSS => 70%

# Nested For Loop Example
students = {
    "Yossef": {"Python": "90%", "HTML": "80%"},
    "Sameh": {"Python": "85%", "CSS": "75%"}
}
for name in students:
    print(f"{name} Skills:")
    for skill in students[name]:
        print(f"- {skill}: {students[name][skill]}")
# Output:
# Yossef Skills:
# - Python: 90%
# - HTML: 80%
# Sameh Skills:
# - Python: 85%
# - CSS: 75%

# ========================================================================================= #
# -----------------------------
# range() function
# -----------------------------
# range(stop) => from 0 to stop-1
# range(start, stop) => from start to stop-1
# range(start, stop, step) => with step increment or decrement

print(list(range(5)))        # [0, 1, 2, 3, 4]
print(list(range(2, 6)))     # [2, 3, 4, 5]
print(list(range(1, 10, 3))) # [1, 4, 7]

# Negative step
print(list(range(5, 0, -1))) # [5, 4, 3, 2, 1]

# ========================================================================================= #
# -----------------------------
# Loop => While
# -----------------------------
# while condition:
#     block of code
# Runs until condition becomes False

a = 1
while a < 5:
    print(a, end=" ")
    a += 1
# Output: 1 2 3 4

# Forgetting to update the loop condition → Infinite Loop
# while True:
#     print("This will never end unless break is used!")

# ========================================================================================= #
# -----------------------------
# Break and Continue
# -----------------------------
# break => exit the loop immediately
# continue => skip current iteration and move to the next

# Break Example
for i in range(1, 6):
    if i == 3:
        break
    print(i, end=" ")
# Output: 1 2

# Continue Example
for i in range(1, 6):
    if i == 3:
        continue
    print(i, end=" ")
# Output: 1 2 4 5

# ========================================================================================= #
# -----------------------------
# else in Loop
# -----------------------------
# The else block executes if the loop finishes normally
# NOTE (without break). It works with both for and while.

for i in range(3):
    print(i, end=" ")
else:
    print("Loop finished without break")
# Output: 0 1 2 Loop finished without break

for i in range(3):
    if i == 1:
        break
    print(i, end=" ")
else:
    print("Loop finished without break")
# Output: 0   (else not executed because of break)

# ========================================================================================= #
# -----------------------------
# pass Statement
# -----------------------------
# 'pass' does nothing. It's a placeholder.
# Used when a statement is required syntactically,
# but you don't want to write code yet.
# Benefit: helps to avoid syntax errors and keeps code structure valid.

if True:
    pass   # placeholder for future code

for i in range(3):
    pass   # maybe later you will add code here

while False:
    pass   # avoids syntax error even with empty body
#=============================================================================================#
# Example:
my_list = ["apple", "banana", "cherry"]

# Using a simple for loop
for item in my_list:
    print(item)

# Output:
# apple
# banana
# cherry
my_dict = {"name": "Yossef", "age": 21, "city": "Mansoura"}

# Using .items() to get key and value
for key, value in my_dict.items():
    print(key, ":", value)

# Output:
# name : Yossef
# age : 21
# city : Mansoura
#=============================================================================================== #
