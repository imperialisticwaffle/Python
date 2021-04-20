# We can add lists to lists.
num_grid = [
    [1, 2, 3], # 0th row
    [4, 5 ,6], # 1st row
    [7, 8, 9], # 2nd row
    [0] # 3rd row. Same convention for the columns.
]

print(num_grid[0][0]) # This returns the entry in the 0th row and 0th column.

# Nested loops are loops inside of loops; we can use them to print out all the elements in this 2d list.
for row in num_grid:
    print(row) # This just prints out what we have above.

# This is the complete nested for loop:
for row in num_grid:
    for column in row:
        print(column)
