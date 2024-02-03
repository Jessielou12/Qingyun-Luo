# break_words：Divide the input sentences into single words according to Spaces
def break_words(stuff) :
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

# sort_words:Sort the words in alphabetical order    
def sort_words(words):
    u"""Sorts(分类) the words."""
    return sorted(words)

# print_first_word：Print the first word    
def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print(word)

# print_last_word：Output (and remove) the last word
def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print(word)
    
# sort_sentence：   
def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sorted(words)

# print_first_and_last：Break sentences into words and print the first and last word
def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

# print_first_and_last_sorted：Separate sentences into words, print the first and last words, and sort them last  
def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
