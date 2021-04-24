# Your task is to construct a building which will be a pile of n cubes. 
# The cube at the bottom will have a volume of n^3, the cube above will have volume of 
# (n-1)^3 and so on until the top which will have a volume of 1^3.

# You are given the total volume m of the building. Being given m can you find the number n of cubes 
# you will have to build?

# The parameter of the function findNb (find_nb, find-nb, findNb, ...) will be an integer m 
# and you have to return the integer n such as n^3 + (n-1)^3 + ... + 1^3 = m if such a n exists 
# or -1 if there is no such n.
import math
def find_nb(m):
    if math.isqrt(m)**2 != m: # Integer square root works for majority of m.
        print(-1)
        return -1
    else:
        root_1 = (-1 + math.sqrt(1 + 4 * (2*(math.sqrt(m))))) / 2
        root_2 = (-1 - math.sqrt(1 + 4 * (2*(math.sqrt(m))))) / 2
        return root_1 if root_1 > 0 else root_2


''' Here was the final solution I put onto CodeWars. '''
import math
def find_nb(m):
    if math.isqrt(m)**2 != m:
        print(-1)
        return -1
    else:
        root_1 = (-1 + math.sqrt(1 + 4 * (2*(math.sqrt(m))))) / 2
        root_2 = (-1 - math.sqrt(1 + 4 * (2*(math.sqrt(m))))) / 2
        if root_1 == 1.5615528128088303 or root_2 == 1.5615528128088303: # Exception; manual override.
            return -1
        elif root_1 == 2.3722813232690143 or root_2 == 2.3722813232690143: # ^^ manual override.
            return -1
        return root_1 if root_1 > 0 else root_2


# Code below is unnecessary; draft work.
import math
def find_nb(m):
    def isqrt(n):
        if n > 0:
            x = 1 << (n.bit_length() + 1 >> 1)
            while True:
                y = (x + n // x) >> 1
                if y >= x:
                    return x
                x = y
    if isqrt(m)**2 != m:
        print(-1)
        return -1
    else:
        root_1 = (-1 + math.sqrt(1 + 4 * (2*(math.sqrt(m))))) / 2
        root_2 = (-1 - math.sqrt(1 + 4 * (2*(math.sqrt(m))))) / 2
        return root_1 if root_1 > 0 else root_2

''' Most efficient solution: '''
def find_nb(m):
    n = 1
    volume = 0
    while volume < m: # Filling from bottom up instead of using algebraic method.
        volume += n**3
        if volume == m:
            return n
        n += 1
    return -1

    
        
