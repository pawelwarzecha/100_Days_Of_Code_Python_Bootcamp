import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for index, row in df.iterrows()}

def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        word_in_nato = [nato_dict[letter] for letter in word]
    except KeyError:
        print("Please only enter letters in the alphabet")
        generate_phonetic()
    else:
        print(word_in_nato)

generate_phonetic()
