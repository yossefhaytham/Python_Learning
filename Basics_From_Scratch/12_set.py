# ============================================================
# SETS
# ============================================================
# [1] Set Items Are Enclosed in Curly Braces {}
# [2] Set Items Are Not Ordered And Not Indexed
# [3] Set Indexing and Slicing Cannot Be Done
# [4] Set Has Only Immutable Data Types (Numbers, Strings, Tuples)
#     => List and Dict Are not Allowed
# [5] Set Items Are Unique
# [6] Do Not Support Concatenation Or Repeat
# [7] Main Methods:
#     - remove(item) => error when item not found in set 
#     - pop()
#     - add(item)
#     - update(iterable)
#     - discard(item) => if item does not exist, no error like remove,pop in list.....
# ============================================================
# -----------------------------
# Basic Example
# -----------------------------
set_one = {"yossef", 18, "mansoura"}
set_one.add(1)
set_one.update([1, 2, 3, 4, 5, 6])  # takes iterable (list/tuple/set) and adds items in it to set
set_one.discard(1)                  # remove item if exists (no error if not)
print(set_one)                      # order changes every run (unordered)
# ======================
# FROZENSET
# ======================
# frozenset() => immutable version of set
# - Stores unique and unordered elements.
# - Unlike set, it cannot be modified (no add(), remove(), discard()).
# - Useful when a constant and unchangeable set of items is needed.
# - Because it is immutable and hashable, it can be used:
#   * As a dictionary key
#   * As an element inside another set

# Create a frozenset
fs = frozenset([1, 2, 3, 4])
print(fs)        # Output: frozenset({1, 2, 3, 4})

# Attempting to modify will raise an error
# fs.add(5)      # AttributeError
# fs.remove(2)   # AttributeError

# Valid operations: membership test, iteration, length
print(2 in fs)   # Output: True
print(len(fs))   # Output: 4

# Example of using frozenset as a dictionary key
d = {frozenset([1, 2]): "value"}
print(d[frozenset([1, 2])])   # Output: value

# -----------------------------
# Immutable Items Only
# -----------------------------
set_two = {"yossef", 18, "mansoura", (1, 2, 3)}  
# NOTE: list or dict cannot be added to set
print(set_two)

# -----------------------------
# Set Operations
# -----------------------------
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Union
# If union of 3 sets => a.union(b, c)
print("Union (|):", set1 | set2)       # set1.union(set2)

# Intersection
print("Intersection (&):", set1 & set2)  # set1.intersection(set2)

# Difference
print("Difference (-):", set1 - set2)    # set1.difference(set2)

# Symmetric Difference
# = (a-b) U (b-a)
print("Symmetric Difference (^):", set1 ^ set2)  # set1.symmetric_difference(set2)

# -----------------------------
# Update Variants
# -----------------------------
# difference_update    => Keep only items not in other set
# intersection_update  => Keep only items also in other set
# symmetric_difference_update => Keep only items not in both sets

# -----------------------------
# Relations Between Sets
# -----------------------------
# issuperset() → Returns True if current set contains all items of given set
# Example:
print({1, 2, 3, 4}.issuperset({1, 2}))   # True

# issubset() → Returns True if current set is fully contained in given set
# Example:
print({1, 2}.issubset({1, 2, 3, 4}))     # True

# isdisjoint() → Returns True if two sets have no elements in common
# Example:
print({1, 2}.isdisjoint({3, 4}))         # True
