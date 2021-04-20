numbers = [36, 24, 8, 9, 15, 18, 28]
friends = ["Ryan", "Jack", "Michael", "Jason", "Andrew"]

# Functions for lists:
friends.extend(numbers) # Adds elements of second list to first.
print(friends)

friends = ["Ryan", "Jack", "Michael", "Jason", "Andrew"]
friends.append("Wallace") # Adds another singular element to the list.
print(friends)

friends = ["Ryan", "Jack", "Michael", "Jason", "Andrew"]
friends.insert(1, "Kevin") # Adds an element at the indicated index point.
print(friends)

friends = ["Ryan", "Jack", "Michael", "Jason", "Andrew"]
friends.remove("Jack") # Removes indicated entry.
print(friends)

friends = ["Ryan", "Jack", "Michael", "Jason", "Andrew"]
# friends.clear()  NOT A FUNCTION IN VSCODE.
print(friends)

friends = ["Ryan", "Jack", "Michael", "Jason", "Andrew"]
friends.pop() # "Pops off" last entry.
print(friends)

friends = ["Ryan", "Jack", "Michael", "Jason", "Andrew"]
print(friends.index("Jack")) # Indicates what index number "Jack" is.

friends = ["Ryan", "Jack", "Michael", "Michael", "Jason", "Andrew"]
print(friends.count("Michael"))

friends = ["Ryan", "Jack", "Michael", "Jason", "Andrew"]
friends.sort() # Sorts by alphabetical.
print(friends)
numbers.sort() # Sorts by increasing.
print(numbers)

numbers.reverse()
print(numbers) # Reverses list order.

friends2 = friends.copy() # NOT A FUNCTION IN VSCODE
print(friends2)