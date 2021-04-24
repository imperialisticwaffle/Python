# We are going to square every digit in a number and concatenate them into an integer.
def square_digits(num):
    digit_sqr = []
    for digit in str(num):
        digit_sqr.append(str((int(digit) * int(digit))))
    new_num = int("".join(digit_sqr))
    print(new_num)
    return new_num
square_digits(int(input("Input a number. ")))

# More efficient solution.
def square_digits(num):
    ret = ""
    for x in str(num):
        ret += str(int(x)**2)
    return int(ret)