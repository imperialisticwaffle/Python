# Isograms have no repeating letters consecutive or otherwise.
string = str(input("Input a word. "))
def is_isogram(string):
    word = []
    for letter in string:
        if letter.lower() in word or letter == "":
            return False
        else:
            word.append(letter)
    return True
is_isogram(string)
