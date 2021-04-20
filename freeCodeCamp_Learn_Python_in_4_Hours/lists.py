# Lists are structures to store lists of information to be used in the program. Denoted with []
friends = ["Ryan", "Jack", "Michael", "Jason", "Andrew"]
    # You can change any entry to a number or boolean.
list1 = ["Name", 3, True]

# We can index lists with the [#] function.
print(friends[0]) # This should return "Ryan", the first entry.
    # Indexing with a negative [-1] starts the index from the end of the list.
print(friends[-1]) # This gives "Andrew".

# We can index lists from an entry onwards.
print(friends[2:])
# Likewise we can go from a certain entry up to but not including another.
print(friends[2:4])

# We can modify entries after defining the list.
friends = ["Ryan", "Jack", "Michael", "Jason", "Andrew"]
friends[2] = "Jasmine"
print(friends) 