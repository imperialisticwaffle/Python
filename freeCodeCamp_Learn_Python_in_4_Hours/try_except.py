# We don't want random slipups to mess up our code. That's why we use try / except functions.
number = float(raw_input("Input a number. ")) # Entering non-number values will break the program.
print(number) 

# We can use a try / except to solve this.
try:
    number = float(raw_input("Input a number. "))
    print(number) 
except:
    print("Invalid input.")

# We can specify multiple errors.
try: 
    number = float(raw_input("Input a number. "))
    print(number) 
    value = 10/0
    print(value)
except ZeroDivisionError:
    print("Undefined - division by zero attempted")
except ValueError:
    print("Invalid input. Use a number")

# We can store specific errors as variables.
try: 
    number = float(raw_input("Input a number. "))
    print(number) 
    value = 10/0
    print(value)
except ZeroDivisionError as err:
    print(err)
except ValueError as err1:
    print(err1)
