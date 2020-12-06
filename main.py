import pandas as pd


# Create a dictionary in this format:
nato_alphabet_data = pd.read_csv("nato_phonetic_alphabet.csv")
nato_alphabet = {row.letter: row.code for (
    index, row) in nato_alphabet_data.iterrows()}


# Create a list of the phonetic code words from a word that the user inputs.
def generate_NATO_spelling():
    word = input("Enter a word: ").upper()
    try:
        nato_spelling = [nato_alphabet[letter] for letter in word]
    except KeyError:
        print("Sorry, only works with letters in NATO code alphabet")
        generate_NATO_spelling()
    else:
        print(nato_spelling)


generate_NATO_spelling()
