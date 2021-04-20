# We will start by creating a function.
def max_num(num1, num2, num3): # Now we can insert an if statement inside the function.
    if num1 >= num2 and num1 >= num3: # The result of these comparisons are True or False (boolean values)
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3 # Since we can assume that if num1 and num2 are not the greatest, num3 is.

print(max_num(5, 15, 7))

# Other comparisons include "==" (equal to); "!=" (not equal to)