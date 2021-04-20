# First, we can start with a boolean variable.
is_male = True

# Then, we define an if statement.
if is_male:
    print("You are a male.") # If statements only return indented code if the boolean variable is true.

# "Otherwise" is represented by else statements.
else:
    print("You are not a male.")

# Demonstrating other scenario...
is_male = False
if is_male:
    print("You are a male.")
else:
    print("You are not a male.")

# With multiple variables...
is_male = True # If one of these boolean variables is false, the "or" statement will still print.
is_tall = True 
if is_male or is_tall: # If either male or tall...
    print("You are a male, or tall, or both.")
else:
    print("You are neither male nor tall.") # If either male or tall...otherwise, they are neither male nor tall.

is_male = True # Both boolean variables MUST be true.
is_tall = True 
if is_male and is_tall: 
    print("You are a tall male.")
else:
    print("You are either not male, not tall, or not both.")

# Adding "else if (elif)" statements...
is_male = False    
is_tall = True 
if is_male and is_tall: 
    print("You are a tall male.")
elif is_male and not is_tall:
    print("You are a short male.")
elif not is_male and is_tall:
    print("You are tall, but not a male.")
else:
    print("You are not a male and not tall.")