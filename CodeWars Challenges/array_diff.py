# Implement a difference function, which subtracts one list from another and returns the result.
# It should remove all values from list a, which are present in list b while keeping their order.
def array_diff(a, b):
    diff = []
    for ele in a:
        if ele not in b:
            diff.append(ele)
    return diff

# Most efficient solution:
def array_diff(a, b):
    return [x for x in a if x not in b]