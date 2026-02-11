# [1] Dict Items Are Enclosed in Curly Braces {}
# [2] Dict Items Are Contains Key : Value
# [3] NOTE Dict Key Need To Be Immutable => (Number, String, Tuple) List Not Allowed
# [4] NOTE Dict Value Can Have Any Data Types
# [5] Dict Key Need To Be Unique
# [6] Dict Is Not Ordered You Access Its Element With "Key"

user = {
    "name": "yossef",
    "age": 18,
    "country": "mansoura",
    "skills": ["c#", "python"],
    "rating": 8
}
print(user["name"])  # output: "yossef"

# Dict["key"] = value → If the key exists, the value will be updated; 
# if it doesn't exist, the key-value pair will be added.
user["name"] = "yassin"

print(user["name"])  # output: "yassin"

# Two-Dimensional Dictionary
# Instead of writing the values inside the dictionary (language) 
# I can make dictionaries and add these name in value 
languages = {
    "One": {
        "name": "python",
        "progress": "60%"
    },
    "Two": {
        "name": "c#",
        "progress": "90%"
    },
    "Three": {
        "name": "html",
        "progress": "90%"
    }
}

# Define each language dictionary
# one = {
#     "name": "python",
#     "progress": "60%"
# }
# two = {
#     "name": "c#",
#     "progress": "90%"
# }

# three = {
#     "name": "html",
#     "progress": "90%"
# }

# # Use the dictionaries as values in the main languages dictionary
# languages = {
#     "One": one,    # this refers to the python dictionary
#     "Two": two,    # this refers to the c# dictionary
#     "Three": three # this refers to the html dictionary
# }

# # Print the result to check
# print(languages)

print(languages["One"]["progress"])   # output: 60%
print(len(languages))                 # output: 3
print(len(languages["Two"]))          # output: 2

# dict.popitem() ====> return last item i was add and delete it
print(languages.popitem())  
# output: ('Three', {'name': 'html', 'progress': '90%'})

# dict.items() return all thing in dict
print(languages.items())  
# output: dict_items([('One', {'name': 'python', 'progress': '60%'}), ('Two', {'name': 'c#', 'progress': '90%'})])

# dict.setdefault(key, value)  
# if it found key, it will return the value; 
# if it doesn't exist, the key-value pair will be added.
print(languages.setdefault("Four", "css"))
print(languages)  
# output: {'One': {'name': 'python', 'progress': '60%'}, 'Two': {'name': 'c#', 'progress': '90%'}, 'Four': 'css'}

# dict.update(["key": value])  ==  dict["key"] = value

# dict.keys()   =====> return all keys
# dict.values() =====> return all values
# -----------------------------
# NOTE Tuples As Dictionary Keys
# -----------------------------
# Dictionary keys must be immutable (cannot change).
# Immutable types include: numbers, strings, and tuples.
# Mutable types (like lists, sets, and dictionaries) are NOT allowed as keys.

# Valid examples with immutable keys
d = {
    1: "number key",
    "name": "string key",
    (10, 20): "tuple key"
}

print(d[1])         # Output: number key
print(d["name"])    # Output: string key
print(d[(10, 20)])  # Output: tuple key

# Invalid example with mutable key
# This will raise an error because lists are mutable
# d = {[1, 2]: "list key"}  
# TypeError: unhashable type: 'list'

# Important NOTE:
# Tuples can be used as keys only if all their elements are immutable.
good = {(1, 2, 3): "ok"}   # Valid
print(good)

# bad = {([1, 2], 3): "no"}  # Invalid because list inside tuple is mutable

