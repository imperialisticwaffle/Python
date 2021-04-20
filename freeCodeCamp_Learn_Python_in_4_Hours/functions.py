# A function is a collection of code that performs a specific task. 
    # You can store code inside a function and call on the function to execute the code.
# We use def to write a function.
"def say_hi():"
    # All the code that comes after the colon goes inside the function.
    # WE NEED TO INDENT FUNCTIONS. TO RUN FUNCTIONS, WE MUST CALL THEM (type out the name and brackets)
def say_hi():
    print("Hello, user!")
say_hi()

# If functions are defined above other code, Python will run from top to bottom.
    # When it reaches the function call it will jump back up to "def" above.

# We can pass (multiple) variables into a function.
def say_hi2(name):
    print("Hello " + name + "!")
say_hi2("Mike")
say_hi2("Steve")

def say_hi3(name, age):
    print("Hello " + name + "! You are " + age + " years old.")
say_hi3("Mike", str(16))

# OR
def say_hi4(name, age):
    print("Hello " + name + "! You are " + str(age) + " years old.")
say_hi4("Mike", 16)

name_input = str(input("What is your name? "))
age_input = str(input("What is your age? "))
def say_hi5(name_input, age_input):
    print("Hello, " + name_input + "! You are " + str(age_input) + " years old.")
say_hi5(name_input, age_input)