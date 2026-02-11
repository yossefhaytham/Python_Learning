# ================================================================
#                             ERRORS
# ================================================================
#
# - SYNTAX ERROR:   Detected during parsing/compilation phase. The code
#                   cannot be executed at all (Python raises SyntaxError
#                   before running).
#                   Syntax errors are like grammatical mistakes.
#                   Example: missing parentheses, colons, indentation errors.
#
# - RUNTIME ERROR:  Happens while the program is running (runtime).
#                   The interpreter starts executing instructions, then
#                   an exceptional condition occurs (ZeroDivisionError,
#                   IndexError, ValueError, etc.).
#
# - LOGIC ERROR:    The program runs without exceptions but produces
#                   wrong or unexpected results because the algorithm
#                   or logic is incorrect.
# ================================================================

# -----------------------
# 1) SYNTAX ERROR example
# -----------------------
# This kind of error is found by Python BEFORE execution (parse time).
# If you try to run the following line, Python will refuse to run it
# and will raise SyntaxError immediately.

# print("Hello"   # <- SyntaxError: invalid syntax (happens before runtime)

# ---------------------------------------------------
# 2) RUNTIME ERROR example
# ---------------------------------------------------
# These errors occur during execution. Python starts running the code,
# then hits an operation that cannot complete and raises an exception.
# Example: ZeroDivisionError happens when the division executes.

def divide(a, b):
    # This function is syntactically valid, so Python will compile it.
    # The division operation is executed at runtime.
    return a / b

try:
    print("Runtime example: dividing 10 by 0...")
    print(divide(10, 0))  # At this line, during execution, ZeroDivisionError is raised
except ZeroDivisionError as e:
    print("Caught runtime error:", type(e).__name__, "-", e)


# -----------------------------------------------------------
# 3) LOGIC ERROR example
# -----------------------------------------------------------
# Logic errors are not reported by Python at all. The program runs
# successfully (no exceptions), but result is incorrect because the
# implementation is wrong (wrong algorithm / wrong operator).
#
# They are discovered by testing, inspection, or wrong outputs.

def add_numbers_wrong(a, b):
    # Logical mistake: subtraction is used instead of addition.
    # This function compiles and runs fine (no exceptions),
    # but its output is logically incorrect.
    return a - b

result = add_numbers_wrong(5, 3)
print("Logic example: expected 8 but got ->", result)  # shows wrong result, no exception


# -----------------------
# Summary (one-line each)
# -----------------------
# SyntaxError  -> Detected at parse/compile time; program doesn't start.
# RuntimeError -> Detected during execution; raises exceptions at the failing statement.
# LogicError   -> Detected after execution by observing incorrect behavior/output; but program will complete run.

# ================================================================
#               Detailed Runtime Errors (Exceptions)
# ================================================================
#
# Runtime errors occur WHEN THE PROGRAM IS RUNNING.
# The code is syntactically correct, so Python starts executing it.
# But during execution, something unexpected happens that Python
# cannot complete → so it raises an exception.
#
# Below are the most common runtime errors with clear explanations.
# ================================================================

# --------------------------
# 1) TypeError Explanation
# --------------------------
#
# A TypeError happens when you try to perform an operation on
# incompatible data types.
#
# Think of it like this:
#   "Imagine trying to add an apple and a banana. That makes no sense."
# In Python:
#   5 + "hello"
# Numbers and strings cannot be added together, so Python gets confused.

print("\n--- TypeError Example ---")
try:
    result = 5 + "hello"  # invalid operation between different types
except TypeError as e:
    print("Caught:", type(e).__name__, "-", e)

# ------------------------------
# 2) AttributeError Explanation
# ------------------------------
#
# AttributeError happens when you ask an object to do something
# it was not designed to do.
#
# Think of it like this:
#   "Imagine you have a toy car, and you tell it to fly. Toy cars don't fly."
# In Python:
#   x = 5
#   x.append(3)
# Integers don't have an 'append' method, so Python raises AttributeError.

print("\n--- AttributeError Example ---")
try:
    x = 5
    x.append(3)  # int has no append() method
except AttributeError as e:
    print("Caught:", type(e).__name__, "-", e)

# --------------------------
# 3) ZeroDivisionError
# ---------------------------
#
# Occurs when dividing by zero during execution.

print("\n--- ZeroDivisionError Example ---")
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print("Caught:", type(e).__name__, "-", e)

# ---------------------------
# 4) IndexError
# ---------------------------
# Happens when accessing a list index that does not exist.

print("\n--- IndexError Example ---")
try:
    nums = [1, 2, 3]
    print(nums[10])  # index out of range
except IndexError as e:
    print("Caught:", type(e).__name__, "-", e)

# ---------------------------
# 5) KeyError
# ---------------------------
# Occurs when accessing a non-existing dictionary key.

print("\n--- KeyError Example ---")
try:
    d = {"name": "Youssef"}
    print(d["age"])  # key does not exist
except KeyError as e:
    print("Caught:", type(e).__name__, "-", e)

# ---------------------------
# 6) ValueError
# ---------------------------
#
# Happens when a value is of correct TYPE but invalid CONTENT.

print("\n--- ValueError Example ---")
try:
    num = int("abc")  # cannot convert letters to int
except ValueError as e:
    print("Caught:", type(e).__name__, "-", e)

# ================================================================
#                How to Handle Errors in Python
# ================================================================
#
# try:       Block of code where we "try" something risky.
# except:    Catches the error so the program does not crash.
# else:      Runs ONLY if no exception happened.
# finally:   Always runs (whether there was an error or not).

# "raise" is used to manually trigger an exception.
# You use it when *you* want to stop execution because something
# is wrong or invalid.
#
# Example:
#   if b == 0:
#       raise ZeroDivisionError("You cannot divide by zero manually!")
#
# After raise, Python immediately jumps to the nearest except block.
#
# We also show how to extract:
#   - the error name
#   - the error message
#   - the line number where the error occurred (using traceback)
# ================================================================
print("\n--- Example: Handling AttributeError ---")

import traceback
try:
    x = 5
    x.append(3)       # <-- AttributeError will happen here
except AttributeError as e:
    # Name of the error
    error_name = type(e).__name__

    # Error message only
    error_msg = str(e)

    # Full traceback (includes line number)
    full_trace = traceback.format_exc()

    print("Error Name:", error_name)
    print("Error Message:", error_msg)
    print("Full Traceback (shows line number):")
    print(full_trace)
# ================================================================
#         Handling errors using multiple except blocks
# ================================================================
print("\n--- Example: Multiple Except Blocks ---")

try:
    result = 10 / 0     # ZeroDivisionError
except ZeroDivisionError:
    print("Cannot divide by zero!")
except TypeError:
    print("Wrong types used!")
# ================================================================
#      Using else (when no errors happen) and finally (always run)
# ================================================================
print("\n--- Example: else and finally ---")

try:
    a = 5 + 3
except Exception:
    print("An error happened!")
else:
    print("No errors occurred, result =", a)
finally:
    print("This block ALWAYS runs.")
    
# ================================================================
#     Catch ANY error (generic catching using Exception as e)
# ================================================================
print("\n--- Example: Catching ALL errors safely ---")

try:
    int("abc")    # ValueError
except Exception as e:
    print("Caught:", type(e).__name__, "-", e)
