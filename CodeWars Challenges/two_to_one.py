# Here, I will take any two words and form the longest possible alphabeticalstring using nonrepeated 
# letters from both words.
def longest(a1, a2):
    new_word = []
    x = len(new_word)
    for letter in a1:
        if letter.lower() in new_word:
            continue
        else:
            new_word.append(letter)
    for letter in a2:
        if letter.lower() in new_word:
            continue
        else:
            new_word.append(letter)
    new_word.sort()
    string = "".join(new_word) # Function for combining elements of a list into a single string.
    print(string)
    return string

longest(input("Input a word. "), input("Input a second word. "))

# Inefficient probably but it gets the job done!
# Apparently this is the most efficient code...
def longest(a1, a2):
    return "".join(sorted(set(a1 + a2))) # Sets are distinct values! Sorted function turns to
    # sorted list.