# ===============================================
# Mutable Data Types (list, set, dict)
# Objects can be changed after creation
# ===============================================

# ---------- LIST ----------
# A list is an ordered, mutable collection of items.
# We can add, remove, or change elements inside it.

nums = [1, 2, 3]
print("LIST Example:")
print("Initial id:", id(nums))

nums.append(4)   # Add element
print("After append:", nums, " | id:", id(nums))

nums.remove(2)   # Remove element
print("After remove:", nums, " | id:", id(nums))

d = nums         # d points to the same list
d.append(5)
print("d and nums point to same object:", id(d) == id(nums))
print("nums after modifying d:", nums)
print("-" * 40)


# ---------- DICTIONARY ----------
# A dictionary is a mutable collection of key-value pairs.
# We can add, update, or delete keys.

info = {"name": "Youssef", "age": 21}
print("DICTIONARY Example:")
print("Initial id:", id(info))

info["city"] = "Mansoura"   # Add key
print("After adding key:", info, " | id:", id(info))

del info["age"]             # Delete key
print("After deleting key:", info, " | id:", id(info))

d = info
d["language"] = "Python"
print("d and info point to same object:", id(d) == id(info))
print("info after modifying d:", info)
print("-" * 40)


# ---------- SET ----------
# A set is an unordered, mutable collection of unique elements.
# We can add or remove elements.

s = {1, 2, 3}
print("SET Example:")
print("Initial id:", id(s))

s.add(4)   # Add element
print("After add:", s, " | id:", id(s))

s.remove(2)   # Remove element
print("After remove:", s, " | id:", id(s))

d = s
d.add(5)
print("d and s point to same object:", id(d) == id(s))
print("s after modifying d:", s)
print("-" * 40)


# ===============================================
# Immutable Data Types (int, string, tuple, range)
# Objects cannot be changed once they are created
# ===============================================

# ---------- INTEGER ----------
# Integers are immutable.
# Any change creates a new object in memory.

x = 1
print("INTEGER Example:")
print("Initial id:", id(x))

x = 19
print("After reassignment:", x, " | id:", id(x))

x = 5
y = 6
print("x id:", id(x), " | y id:", id(y))
print("x and y point to same object?", id(x) == id(y))
print("-" * 40)


# ---------- STRING ----------
# Strings are immutable.
# Any modification creates a new object.

text = "hello"
print("STRING Example:")
print("Initial id:", id(text))

text = text + " world"
print("After concatenation:", text, " | id:", id(text))

new_text = "hello world"
print("new_text id:", id(new_text))
print("Same object?", id(text) == id(new_text))
print("-" * 40)


# ---------- TUPLE ----------
# A tuple is an immutable ordered collection.
# Elements cannot be added or removed.

t = (1, 2, 3)
print("TUPLE Example:")
print("Initial id:", id(t))

t = t + (4,)  # Creates a new tuple
print("After concatenation:", t, " | id:", id(t))
print("-" * 40)


# ---------- RANGE ----------
# A range is an immutable sequence of numbers.
# It is usually used in loops.

r = range(1, 4)
print("RANGE Example:")
print("Initial id:", id(r))
print(r)

r = range(1, 6)  # New range object
print("After changing range:", list(r), " | id:", id(r))
print("-" * 40)

