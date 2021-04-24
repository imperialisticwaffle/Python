
n = int(input("Please input a random positive integer. "))
def digital_root(n):
    if n < 10:
        print(n)
        return
    else:
        sum_of_digits = 0
        for digit in str(n):
            sum_of_digits += int(digit) # Up until here in the code, it works. 98 doesn't work, for example.
        if sum_of_digits >= 10:
            new_sum = 0
            while sum_of_digits >= 10:
                for digit_2 in str(sum_of_digits):
                    new_sum += int(digit_2)
            print(new_sum)
            return 
        else:
            print(sum_of_digits)
            return sum_of_digits
digital_root(n)

n = int(input("Please input a random positive integer. "))
def digital_root(n):
    if n < 10:
        print(n)
        return
    else:
        sum_of_digits = 0
        for digit in str(n):
            sum_of_digits += int(digit) # Up until here in the code, it works. 98 doesn't work, for example.
        if len(str(sum_of_digits)) >= 2:
            print("loop enter") # infinite loop test
            while len(str(sum_of_digits)) >= 2:
                for digit in str(sum_of_digits):
                    sum_of_digits += int(digit)
                if len(str(sum_of_digits)) == 1:
                    break
            print("loop exit") # infinite loop test
            print(sum_of_digits)
            return sum_of_digits
    return
      
digital_root(n)

# TIL n mod 9 is the digital root. If n divisible by 9, DR is 9.
n = int(input("Please input a random positive integer. "))
def digital_root(n):
    if n % 9 == 0 and not n == 0:
        print("The digital root of", n, "is 9") 
    elif n % 9 > 0:
        print("The digital root of", n, "is", n % 9)
    elif n == 0:
        print("The digital root of", n, "is 0") 
    return
digital_root(n)
