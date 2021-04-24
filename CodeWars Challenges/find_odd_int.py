# Program to locate integer appearing odd # of times in list.
from collections import Counter
def find_it(seq):
    if len(seq) == 1:
        print(seq[0])
        return seq[0]
    x = Counter(seq) # Returns dict w/ key (integer) and value (freq)
    value_list = list(x.values()) # Turning values into list for indexing.
    key_list = list(x.keys()) # Turning keys into list for indexing.
    for freq in value_list:
        if freq % 2 == 1:
            place = value_list.index(freq) # Finding index of odd freq in value_list.
            print(key_list[place]) # Corresponding index for integer list. 
            return key_list[place]
sample = [10, 10, 10, 10, 10, 10, 10, 10, 8, 8, 8, 8, 9, 9, 9, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1]
find_it(sample)

# Most efficient solution...
def find_it(seq):
    for i in seq:
        if seq.count(i)%2!=0: # for every integer in the sequence, if the freq (.count()) when divided by
            # 2 =/= (!=) 0, then return integer
            return i












 
