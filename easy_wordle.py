#Cameron Nagle
#Oct 8th 2023
#Easy_Wordle

import words
import wordle
import display_utility
import random

def filter_word_list(words, clues):
    """Takes a list of words and the clues list. It returns a list with only words that could be in the secret word"""
    new_words = []
    clues = dict(clues)
    #Go through each clue and add to x if the clue is true for each word
    for i in words:
        x = 0
        for j in clues:
            i = i.upper()
            if(wordle.check_word(i, j) == clues[j]):
                x += 1
            elif(wordle.check_word(i, j) != clues[j] and i.lower() in new_words):
                x = -1
        #If each clue words for the word then append the word to the list
        if(x == len(clues)):
            new_words.append(i.lower())

    return new_words

def easy_game(secret):
    """Takes in a secret word and returns nothing"""
    guess_num = 0
    clues_list = []
    clues_done = []
    guess = ""
    #While the guess number is less than 6 times and guess does not equal secret
    while(guess_num <= 5 and guess != secret):
        guess = str(input("> ")).upper()
        if(len(guess) == 5):
            guess_num += 1
            if(guess != secret):
                #If the guess is not the secret append the guess to the clues and the clues to the list
                clues_done.insert(0, guess)
                clues_list.append((guess, wordle.check_word(secret, guess)))
                #Go through word and each letter in the clues guessed and print out the letter with the color
                for i in clues_done[::-1]:
                    x = 0
                    for j in i:
                        if(wordle.check_word(secret, i)[x] == "yellow"):
                            display_utility.yellow(j)
                        elif(wordle.check_word(secret, i)[x] == "green"):
                            display_utility.green(j)
                        else:
                            display_utility.grey(j)
                        x += 1
                    print()
                #If there are more than 5 possible words print out a random 5 or else print out the words possible
                if(len(filter_word_list(words.words, clues_list)) > 5):
                    print(len(filter_word_list(words.words, clues_list)), "words possible:")
                    print(random.choices(filter_word_list(words.words, clues_list), k=5))
                else:
                    print(len(filter_word_list(words.words, clues_list)), "words possible:")
                    for i in filter_word_list(words.words, clues_list):
                        print(i.lower())
        else:
            print("Not a word. Try again")
    #If the guess is the secret print out each guess with colors and then the answer
    if(guess == secret):
        clues_done.insert(0, guess)
        for i in clues_done[::-1]:
            x = 0
            for j in i:
                if(wordle.check_word(secret, i)[x] == "green"):
                    display_utility.green(j)
                elif(wordle.check_word(secret, i)[x] == "yellow"):
                    display_utility.yellow(j)
                else:
                    display_utility.grey(j)
                x += 1
            print()
        print("1 words possible:")
        print(guess)
        print("Answer:", guess)


#START THE GAME HERE WITH WHATEVER WORD YOU WANT UNCOMMENT LINE BELOW
#easy_game("GREEN")