name = "yossef"
age = 18
rank = 10
# print("My Name is: " + name + " and My Age is: " + age)  # Type Error
#1
print("My Name is: %s and My Age is: %d and My Rank is: %f" % (name, age, rank))
# %s => String
# %d => Number
# %f => Float

#2
print("My Name is: {} Age: {} & Rank is: {}".format(name, age, rank))

#3
print(f"My Name is : {name} and My Age is : {age}")


