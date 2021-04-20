# Tuples are similar to lists; they are containers to store different values.
    # Tuples use () instead of [], which lists use.
coordinates = (4, 5)
# Tuples are immutable; cannot be changed or modified.
coordinates[1] = 10 # Trying to replace the second entry returns an error.

# We can access entries by indexing how we have before.
print(coordinates[0]) # This returns "4".

# Tuples store data that never needs to be changed (i.e. coordinates).
    # We can create lists of tuples.
coord_list = [(4, 5), (9, 10), (80, 36)] # The entries (tuples) in the list cannot be modified.