# Problem Set 2, hangman.py
# Name: kumarswami boga 
# Collaborators: vaibhav pensalwar

# Time spent:
# Hangman Game

import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for char in secret_word:
        if char not in letters_guessed:
            return False
        
    return True



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    secret_word_to_print = ''
    for char in secret_word:
        if char not in letters_guessed:
            secret_word_to_print += '_ '
        else:
            secret_word_to_print += char
            
    return secret_word_to_print



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    available_letters = ''
    for char in string.ascii_lowercase:
        if char not in letters_guessed:
            available_letters += char
    
    return available_letters
        
    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.
    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    print('##############---------Welcome to the Hangman Game---------#####################')
    print("Game Rules: 1) Guess Input Should be LowerCase Alphabet Letter" )
    print("2) Guess one Input As a Time otherwise One Warning count will be diducted")
    print("After 3 Deduction of Warning 1 Guess will Deducted from guess count")
    print("Play then Game ......Good Luck")
    print('Secret word is ' + str(len(secret_word)) + ' letters long')
    
    
    warnings_left = 3
    letters_guessed = []
    guesses_left = 6
    
    print('You have '+ str(warnings_left) + ' warnings left')
    print('-------')
    
    while True:
        print('You have '+ str(guesses_left) +  ' guesses left')
        print('Available letters: ' + get_available_letters(letters_guessed))
    
        letter_guessed = raw_input('Please enter a letter: ').lower()
        guessed_word = get_guessed_word(secret_word, letters_guessed)
        
        if(letter_guessed.isalpha()):
            if(letter_guessed not in letters_guessed):   
                letters_guessed.append(letter_guessed)
                guessed_word = get_guessed_word(secret_word, letters_guessed)
                
                if(letter_guessed in secret_word):
                    print('Good guess: ' + guessed_word)
                else:
                    if(letter_guessed in 'aeiou'):
                        guesses_left -= 2
                    else:
                        guesses_left -= 1  
                    print('Oops! That letter is not in my word: ' + guessed_word)
            else:
                if(warnings_left > 0):
                    warnings_left -= 1
                    print('Oops! You have already guessed that letter. You now have ' + str(warnings_left) +' warnings:' + guessed_word)
                else:
                    guesses_left -= 1
                    print('Oops! You have already guessed that letter. You now have no warnings left so you lose one guess' + guessed_word)
        elif(letter_guessed == "*"):
            print(show_possible_matches(guessed_word))


        else:
            if(warnings_left > 0):
                warnings_left -= 1
                print('Oops! That is not a valid letter. You have '+ str(warnings_left)+' warnings left: '+ guessed_word)
            else:
                warnings_left -= 1
                print('Oops! You have already guessed that letter. You now have no warnings left so you lose one guess: ' + guessed_word)
    
    
        if(is_word_guessed(secret_word, letters_guessed)):
            unique_letters_in_secret_word = []
            for char in secret_word:
                if char not in unique_letters_in_secret_word:
                    unique_letters_in_secret_word.append(char)
            
            print('Congratulations, you won!')
            print('Your total score for this game is ' + str(guesses_left * len(unique_letters_in_secret_word)))
            break
    
        if(guesses_left <= 0):
            print('Sorry, you ran out of guesses. The word was :' + secret_word)
            break





def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    no_spaces_words = ''
    letters_guessed = []
    for c in my_word:
        if c != ' ':
            no_spaces_words += c
            
        if(c.isalpha()):
            letters_guessed.append(c)
        
    if (len(no_spaces_words.strip()) != len(other_word.strip())):
        return False
    
    for i in range(len(no_spaces_words)):
        current_letter =  no_spaces_words[i]
        other_letter = other_word[i]
        if current_letter.isalpha():
            has_same_letter = current_letter == other_letter
            if not has_same_letter:
                return False
        else:
            if current_letter == '_' and other_letter in letters_guessed:
                return False
            
    return True
    


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.
    '''
    matched_words = []
    for word in wordlist:
        if match_with_gaps(my_word, word):
            matched_words.append(word)

    if len(matched_words) > 0:
        for word in matched_words:
            print(word )
        print()
    else:
        print('No matches found')



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.
    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''




if __name__ == "__main__":
    pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman(secret_word)