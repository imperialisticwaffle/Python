# Let's outline the conditions for our mini-language.
# Random Language:
    # All vowels --> x.
    # Consonants stay the same.

# Now let's build the translator.
new_word = str(raw_input("Enter a word to translate. "))
vowels = ["a", "e", "i", "o", "u"]

def translate(new_word):
    translation = ""
    for letter in new_word:
        if letter.lower() in vowels:
            if letter.isupper():
                translation = translation + "X"
            else:
                translation = translation + "x"
        else:
            translation = translation + letter
    return translation
print(translate(new_word))

# Let's try to make this a bit more advanced. I want to add each new word to a dictionary list and notify users of 
# repeated entries.
# ***Updated note: any code below is incorrect, but I am leaving it as part of my thought process.
    # The full correct version is stored in translator_ELITE_VER.py.
dictionary = []
dictionary_count = 0
translation = ""

def translate(translation):
    for letter in translation:
        if letter.lower() in vowels:
            if letter.isupper():
                translation = translation + "X"
            else:
                translation = translation + "x"
        else:
            translation = translation + letter
        return translation

while len(dictionary) < float("inf"):
    translation = str(raw_input("Enter a word to translate. "))
    translate(translation)
    if translation in dictionary:
            print("This has already been translated.")
            dictionary_count = dictionary_count + 0
    else:
        dictionary.append(translation)
        dictionary_count = dictionary_count + 1
        print(translate(translation))

