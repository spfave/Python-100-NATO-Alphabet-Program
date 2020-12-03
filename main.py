import pandas as pd


# Create a dictionary in this format:
nato_alphabet_data = pd.read_csv("nato_phonetic_alphabet.csv")
nato_alphabet = {row.letter: row.code for (
    index, row) in nato_alphabet_data.iterrows()}

# Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()
nato_spelling = [nato_alphabet[letter] for letter in word]
print(nato_spelling)
