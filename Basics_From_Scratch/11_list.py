# ============================================================
# LISTS
# Lists allow you to store sets of information in one place
# ============================================================

# [1] List Items Are Enclosed in Square Brackets []
# [2] Lists Are Ordered => Use Index To Access Item
# [3] Lists Are Mutable => Add, Delete, Edit
# [4] List Items Are Not Unique
# [5] List Can Have Different Data Types

MyList = ["yossef", 18, True]
print(MyList[0])     # output: "yossef"
# print(MyList[-2])  # output: 18

# ------------------------------------------------------------
# count() method => counts items in list
# ------------------------------------------------------------

# ======================
# ADD
# ======================
MyList.append("adel")          # append() => takes 1 item only, adds it to the end
MyList.extend(["adel", 20, False]) # extend() => takes a list and adds elements to the end
MyList.insert(0, "first")      # insert(index, item) => add item before index
# output: ['first', 'yossef', 18, True, 'adel', 'adel', 20, False]

# ======================
# DELETE
# ======================
# del ... => general deletion by index, slice, or variable
MyList.remove("adel")   # remove() => deletes first occurrence of the value , item is no exsist OUTPUT => error
print(MyList)           # output: ['yossef', 18, True, 'adel', 20, False]
# NOTE: remove() only deletes the first occurrence.
# If the value appears multiple times, use a loop to delete them all.

print(MyList.pop(4))    # pop(index) => remove and return item at that index , it can be IndexOutOfRange index > index of list
MyList.clear()          # clear() => removes all items
print(MyList)           # output: []

# ======================
# EDIT / ORGANIZING
# ======================
x = ["a", "w", "k", "b", "c"]
print(sorted(x))   # sorted() => returns a new sorted list but does NOT change the original
x.sort()           # sort() => sorts the list in-place (only works if elements are the same type)
print(x)           # output: ['a', 'b', 'c', 'k', 'w']

# x.sort(reverse=True) => NOTE sort in descending order............
# NOTE: TypeError if list contains multiple data types

print(list(reversed(x))) #=> returns an iterator (not a list), can be cast with list(reversed(x)),NOTE return list reversible.......
# ======================
#NOTE NOTE NOTE REVERSED
# ======================
# reversed(sequence) => returns an iterator that accesses the sequence in reverse order
# - Works on lists, tuples, strings, and any reversible sequence
# - Does NOT create a new list automatically (returns an iterator)
# - To get a list, wrap it with list(reversed(...))
# - Does not modify the original sequence

nums = [5, 2, 9, 1]

rev = reversed(nums)
print(rev)            # Output: <list_reverseiterator object at ...>
print(list(rev))      # Output: [1, 9, 2, 5]

# Original list is unchanged
print(nums)           # Output: [5, 2, 9, 1]

# Example with string
s = "python"
print(list(reversed(s)))   # Output: ['n', 'o', 'h', 't', 'y', 'p']
print("".join(reversed(s))) # Output: "nohtyp"
#============================================================================
x.reverse()        # reverse() => reverses the list in-place
print(x)

c = [2, 3, 5, 6, 78, 9976]
c.sort(reverse=True)     # sort descending
print(c)

# ======================
# INDEX & COUNT
# ======================
print(c.index(5))     # index(item, start, end) => returns index of the first occurrence
# NOTE: If item does NOT exist => raises ValueError

print(c.count(9976))  # count(item) => number of occurrences
print(len(c))         # len() => number of items in the list

# DIFFERENCE BETWEEN index() and find():
# - index() is used for lists, raises an error if item not found.
# - find() is used for strings, returns -1 if substring not found,but to string only 

# ======================
# SLICING
# ======================
my_list = [1, 2, 3, 4, 5]
print(my_list[1:4])    # output: [2, 3, 4]
print(my_list[:3])     # output: [1, 2, 3]
print(my_list[::2])    # output: [1, 3, 5]
print(my_list[-1::-1]) # output: [5, 4, 3, 2, 1]
