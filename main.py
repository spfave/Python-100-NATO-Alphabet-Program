import pandas as pd

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
nato_alphabet_data = pd.read_csv("nato_phonetic_alphabet.csv")
nato_alphabet = {row.letter: row.code for (
    index, row) in nato_alphabet_data.iterrows()}

print(nato_alphabet)
# {"A": "Alfa", "B": "Bravo"}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
