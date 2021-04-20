# Dictionaries are a structure that allow storage of information in "key value pairs".
    # Keys are like the words of dictionaries; their values are their definitions.
    # Dictionaries take these {} / colons / commas, and require indenting, shown below.
    # Keys can also be numbers.
monthConversions = {
    "Jan": "January", # Left side of colon = key; right side = value. Keys must be unique.
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}
# We can retrieve keys and their values in a number of ways.
print(monthConversions["Jul"])
print(monthConversions.get("Apr")) # For .get() we can create a default value if the key we enter doesn't exist.
# To do this, we use a comma shown below.
print(monthConversions.get("luv", "Not a valid entry."))
