# To obtain input from users we use input().
    # Inside the parentheses we type the string prompt.
# input("Enter your name: ")

# We can then put this into a variable.
name = str(input("Enter your name: "))
print("Hello, " + name + " !")

# Note that string variables can combine with strings, but number variables cannot combine with strings.
# VSCode requires that you put quotations around the name string. Numbers are fine themselves.

# Continuing...
name = str(input("Enter your name: "))
age = str(input("Please enter your age: "))
print("Hello, " + name + "! You are " + age + " years of age.")