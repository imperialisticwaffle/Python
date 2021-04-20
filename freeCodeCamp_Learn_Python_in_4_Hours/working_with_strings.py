# The \n function in the parentheses of a print() function creates a linebreak.
print("Giraffe\nAcademy")

# If you want a quotation mark inside a string (print something literally) use \ (escape character).
print("Giraffe\"Academy")

# You can also print variables.
phrase = "Giraffe Academy"
print(phrase)

# Concatenation - appending a string onto a variable.
print(phrase + " is cool")

# Function - a block of code we can run that performs a specific operation for us. Can modify/get info on strings
print(phrase.lower()) # all lowercase
print(phrase.upper()) # ALL UPPERCASE
print(phrase.isupper())
    # .isupper() or .islower() returns a TRUE or FALSE value if entirely upper/lowercase
print(phrase.upper().isupper())
    # Runs .upper() first (converts to caps) and checks if phrase is all caps.
print(len(phrase))
    # Gives length of string or variable in parentheses

# [#] gives the corresponding letter to the number (#). First letter in string = 0.
print(phrase[0])
# Index function tells where a specific char. or string is located inside given string. OPPOSITE TO ABOVE
print(phrase.index("G"))
    # Putting values inside .index() is called "passing a parameter".
print(phrase.index("Acad"))
    # Gives where "Acad" starts (i.e. 8)
# Putting a nonexistent string/char returns an ERROR.

# We can replace strings too.
print(phrase.replace("Giraffe", "Elephant"))

# YOU CAN LOOK UP STRING FUNCTIONS IN PYTHON ONLINE.