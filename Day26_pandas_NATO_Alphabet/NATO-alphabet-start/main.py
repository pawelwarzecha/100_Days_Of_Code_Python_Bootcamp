import pandas

# Create a dictionary from the csv
df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for index, row in df.iterrows()}

# Prompt a User to enter a word, create a list of each letter in the word, replace letters, print output
word = input("Enter a word: ").upper()
word_in_nato = [nato_dict[letter] for letter in word]
print(word_in_nato)

