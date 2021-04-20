# A variable is a container that stores certain data values. 
# Here is a sample story.
print("There once was a man named George,")
print("he was once 70 years old. ")
print("He really liked the name George ")
print("but he didn't like being 70.")

# If you wanted to change the character's name or age, you would have to manually go into the code/change it.
# This is not efficient; we should use variables here to store name/age.
# Let's define the variables first (spaces denoted by underscore).
character_name = "John"
character_age = "35"

# Variables and strings are different, so when inputting variables we cut off the string (i.e. the comma).
# We also need to have + signs when adding variables and strings. There won't be spaces b/w var & strings.
print("There once was a man named " + character_name + ", ")
print("he was once " + character_age + " years old. ")
print("He really liked the name " + character_name + ", ")
print("but he didn't like being " + character_age + ".")

# If you want to update var's, you need to redefine them above these print() functions.
# You can redefine the character name in the middle of the functions.
print("There once was a man named " + character_name + ", ")
print("he was once " + character_age + " years old. ")
character_name = "Mike"
print("He really liked the name " + character_name + ", ")
print("but he didn't like being " + character_age + ".")

# Variables can store strings, numbers (decimal or whole), or boolean values. BVs are "true or fales" values.
character_name = "John"
character_age = "35"
is_male = True 