# Let's try to make this a bit more advanced. I want to add each new word to a dictionary list and notify users of 
# repeated entries.

# Defining needed variables and lists.
dictionary = []
vowels = ["a", "e", "i", "o", "u"]

while len(dictionary) < float("inf"): # I want to translate infinite words.
    new_word = str(input("Enter a word to translate. "))
    def translate(new_word): # Function for translating.
        translation = "" # Empty string that gets filled as we parse our input letter by letter.
        for letter in new_word: # Parsing input.
            if letter.lower() in vowels:
                if letter.isupper():
                   translation = translation + "X" # Replacing case-sensitive vowels / adding letter to "translation".
                else:
                   translation = translation + "x" # Replacing vowels / adding letter to "translation".
            else:
                translation = translation + letter # No change / adding letter to "translation".
        if translation in dictionary: # If word is already translated.
            print("This word has already been translated:")
            return translation
        else: # If new word.
            dictionary.append(translation)
            return translation
    print(translate(new_word))