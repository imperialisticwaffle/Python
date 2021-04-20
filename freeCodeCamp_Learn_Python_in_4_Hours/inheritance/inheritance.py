# Inheritance is where we can define attributes and functions inside of a class, 
# create another class, and inherit those attributes.
    # Essentially a class has the functionality of another class you define, but more. (easier for big classes)
from chef import Chef
newchef = Chef() # Giving the Chef class attributes to "newchef"
newchef.make_chicken() # Checking if newchef has Chef's attributes.

# Let's assume we want to make another class called "Chinese Chef" that does everything generic "Chef" does.
    # First let's import from chinese_chef.py.
from chinese_chef import Chinese_Chef
new_chinese_chef = Chinese_Chef()
new_chinese_chef.make_fried_rice() # Checking if new_chinese_chef has Chinese_Chef's attributes.

# The more efficient way (without copying and pasting to class Chinese_Chef) is to inherit.
class Chinese_Chef_2(Chef): # Be sure to import the class in the parentheses first.
    def make_special_dish(self):
        print("The chef has made congee.") # Overriding the inherited "chef makes BBQ ribs" attribute.
    def make_fried_rice(self):
        print("The chef has made fried rice.")

new_Chinese_Chef_2 = Chinese_Chef_2() # Don't forget to define an object.
new_Chinese_Chef_2.make_fried_rice() # And the inheritance worked!
