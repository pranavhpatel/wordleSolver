import random

# load list of words possible for the game from file input
def load_words(file_name):
    all_words_list = []

    with open(file_name, "r", newline="") as word_file:
        for word in word_file:
            # format word
            word = word.lower().strip()
            if word.isalpha() and len(word) == 5:
                all_words_list.append(word)
    
    return all_words_list
