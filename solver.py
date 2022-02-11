import random

def get_word(all_words_list,possible_words,ignore_list):
    letter_frequency = {}
    position_frequency = [{}]*6
    # set starting good word then calculate from word score
    top_word = possible_words[0]
    max_frequency,max_position_frequency = 0

    if len(possible_words) < 3:
        # return first word
        return possible_words[0]

    #calculate frequency for letters in possible words
    #brute force loop each word then each letter
    for word in possible_words:
        letters_to_ignore = ignore_list
        position_index = 0
        for letter in word:
            if letter in letters_to_ignore:
                letters_to_ignore = letters_to_ignore.replace(letter,"",1)
            else:
                # add to letter frequency map then increment counter for that
                if letter not in letter_frequency:
                    letter_frequency[letter] = 0
                letter_frequency[letter] +=1
            # add to position frequency for x letter then increment its counter
            if letter not in position_frequency[position_index]:
                position_frequency[position_index][letter] = 0
            position_frequency[position_index][letter] +=1

            # increment position_index for next letter
            position_index +=1
    
    #calculate frequency for letters in all words
    #brute force loop each word then each letter
    for word in all_words_list:
        word_score = 0
        get_set = set()
        letters_to_ignore = ignore_list
        for letter in word:
            if letter in letters_to_ignore:
                letters_to_ignore = letters_to_ignore.replace(letter,"",1)
            else:
                # if letter not in gotten set add it
                if letter in get_set:
                    continue
                get_set.add(letter)
                # if letter is in the frequency list then the score will increment by the frequency for that letter
                if letter in letter_frequency:
                    word_score += letter_frequency[letter]
        
        # check if the current words score is highest, if so make that the top_word
        if word_score > max_frequency:
            max_frequency = word_score
            top_word = word

            # calculate position score
            position_score = 0
            for i in range(len(word)):
                if word[i] in position_frequency[i]:
                    position_score += position_frequency[i][word[i]]
            max_position_score = max_position_frequency

        # get top word based on position score for letters
        elif word_score == max_frequency:
            position_score = 0
            for i in range(len(word)):
                if word[i] in position_frequency[i]:
                    position_score += position_frequency[i][word[i]]

            # update word by the position score for letters in word
            if position_score > max_position_score:
                max_position_score = position_score
                top_word = word

    return top_word


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
