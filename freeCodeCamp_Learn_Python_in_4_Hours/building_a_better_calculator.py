# We will use the float() function again to keep entered values as numbers.
num1 = float(input("Please enter a first numer. "));
op = str(raw_input("Please enter an operation. ")); # raw_input() takes any character, not just numbers.
num2 = float(input("Please enter a second numer. "));

# We can then use an if statement to provide scenarios for different "op" values.
if op == "+" or op == "plus" or op == "addition" or op == "add":
    print(num1 + num2);
elif op == "-" or op == "minus" or op == "subtraction" or op == "subtract":
    print(num1 - num2);
elif op == "x" or op == "*" or op == "multiplication" or op == "multiply" or op == "times":
    print(num1 * num2);
elif op == "divide" or op == "/" or op == "division":
    print(num1 / num2);
elif op == "power" or op == "^" or op == "to the exponent of":
    print(pow(num1, num2));
else:
    print("Invalid operation");
