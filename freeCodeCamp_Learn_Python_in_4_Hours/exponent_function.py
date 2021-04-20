# Double multiplication signs are exponents.
print(2**3) # This gives 8.
# We can make exponent functions also with for loops.
def raise_power(base_num, pow_num): # We could do base_num * base_num...etc. but we don't know what pow_num is.
    result = 1
    for index in range(pow_num):
        result = result * base_num # base_num * 1 = base_num; base_num * base_num = base_num ^ 2; ... base_num ^ (pow_num - 1) * base_num
    return result
print(raise_power(3, 3))

def raise_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result
base_num = input("Input a base number. ")
pow_num = input("Input an exponent. ")
print(raise_power(base_num, pow_num))