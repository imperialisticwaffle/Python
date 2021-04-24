# Given three sides, write a program that determines if a triangle is possible.
def is_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    elif a < 0 or b < 0 or c < 0:
        return False
    else:
        return False
# Using triangle inequality theorem.

# Most efficient solution.
def is_triangle(a, b, c):
    return (a + b) > c and (a + c) > b and (b + c) > a