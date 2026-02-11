# ============================================================
# TUPLES
# ============================================================
# [1] Tuple Items Are Enclosed in Parentheses ()
# [2] Parentheses Can Be Omitted (Python will still treat it as tuple if comma is used)
# [3] Tuples Are Ordered => Use Index To Access Item
# [4] Tuples Are Immutable => Cannot Add or Delete elements
# [5] Tuple Items Can Be Repeated (not unique)
# [6] Tuple Can Contain Different Data Types
# [7] Operators Used in Strings and Lists Are Available in Tuples
# ============================================================

# -----------------------------
# Basic Tuple
# -----------------------------
My_tuple = (1, 2, 3, 4, 5)
print(My_tuple[2])      # Output: 3

# My_tuple[2] = 5
# TypeError: 'tuple' object does not support item assignment

# -----------------------------
# Empty Tuple
# -----------------------------
empty = ()
print(empty)    # Output: ()

# -----------------------------
# One-Item Tuple
# -----------------------------
single = (5,)   # must include a comma
print(type(single))  # <class 'tuple'>

not_tuple = (5)
print(type(not_tuple))  # <class 'int'>

# -----------------------------
# Nested Tuples
# -----------------------------
nested = (1, (2, 3), ["a", "b"])
print(nested[1])   # Output: (2, 3)
print(nested[2])   # Output: ['a', 'b']

# NOTE: tuple is immutable, but if it contains a mutable item (like list), 
# that item can be changed.
nested[2].append("c")
print(nested)   # Output: (1, (2, 3), ['a', 'b', 'c'])

# -----------------------------
# Tuple Methods
# -----------------------------
t = (1, 2, 2, 3, 4)
print(t.count(2))   # count(item) => returns number of times value appears => 2
print(t.index(3))   # index(item) => returns first index of value => 3

# -----------------------------
# Other Operations
# -----------------------------
print(len(t))         # length => 5
print(t[1:4])         # slicing => (2, 2, 3)

t2 = (5, 6)
print(t + t2)         # concatenate => (1, 2, 2, 3, 4, 5, 6)
print(t * 2)          # repeat => (1, 2, 2, 3, 4, 1, 2, 2, 3, 4)

# -----------------------------
# Tuple Unpacking
# -----------------------------
a, b = (10, 20)
print(a, b)   # Output: 10 20

# Extended unpacking
a, *b = (1, 2, 3, 4)
print(a)  # Output: 1
print(b)  # Output: [2, 3, 4]
# -----------------------------
# Tuple As Return Value
# -----------------------------
# A function can return multiple values at once using a tuple.
# Think of a tuple as a "box" that carries more than one answer.

def min_max(seq):
    return min(seq), max(seq)   # returns a tuple (min, max)

result = min_max([3, 1, 4])
print(result)        # Output: (1, 4)

# Tuple unpacking makes it easy to separate the values
low, high = min_max([10, 50, 3])
print(low)   # Output: 3
print(high)  # Output: 50


# -----------------------------
# Tuple Methods (Only 2 Available)
# -----------------------------
# Tuples are immutable, so they have very limited methods.
# Only 2 methods exist:
# [1] count(item) => how many times item appears
# [2] index(item) => first position where item appears

t = (1, 2, 2, 3, 4)

print(t.count(2))   # Output: 2 (2 appears twice)
print(t.index(3))   # Output: 3 (first occurrence of 3 is at index 3)

# NOTE: Unlike lists, tuples do not have append(), remove(), sort(), etc.
# Only count() and index() are available.

