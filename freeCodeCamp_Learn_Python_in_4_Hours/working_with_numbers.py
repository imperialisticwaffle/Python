# Python can print all real numbers.
print(-2.9099239487)

# Python can carry out basic operations.
print(3 + 4)
print(3 - 4)
print(3 / 4)
print(3 * 4)

# BEDMAS also works.
print(3 * (4 + 5))

# Modulates operator (%) gives the remainder of two numbers divided (modular arithmetic).
print(10 % 3)

# You can store numbers as variables.
my_num = 8
    # And then convert it to a string:
print(str(my_num))

# This is important: you cannot combine numbers and strings.
    # print(my_num + " is my favourite number.") returns an error.
print(str(my_num) + " is my favourite number.") # is fine.

# Functions with numbers:
my_num = -5
print(abs(my_num)) # absolute value.
print(pow(my_num, 2)) # -5^2
print(max(4, 6)) # gives the highest number in a set.
print(min(4, 6))
print(round(3.7)) # rounds numbers.

from math import * # THIS GIVES US THE ABILITY TO ACCESS MORE MATH FUNCTIONS.
    # ^ "math" is called a MODULE.
print(ceil(3.2)) # always rounds up
print(floor(3.7)) # always rounds down
print(sqrt(36))

# YOU CAN LOOK UP NUMBER FUNCTIONS IN PYTHON ONLINE.