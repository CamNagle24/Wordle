#Cameron Nagle
#Oct 8th 2023
#Wordle

import display_utility

def check_word(secret, guess):
    """Takes a string of the secret word, a string of the guessed word. It returns a list of the strings"""
    #Make the list of colors grey and the repeat colors a blank list
    color = ["grey"] * 5
    repeat_guess_list = [" "] * 5
    repeat_secret_list = [" "] * 5

    #For each letter in guess and secret put them into a repeat list
    for i in range(5):
        repeat_guess_list[i] = guess[i]
        repeat_secret_list[i] = secret[i]
    
    #If the guess letter is in the same spot as in secret then the color is green in that position
    #Then make that spot in repeat list blank
    for i in range(5):
        if(guess[i] == secret[i]):
            color[i] = "green"
            repeat_guess_list[i] = " "
            repeat_secret_list[i] = " "

    #If the letter is in the repeat list still and the index is not green already(" ") then that spot is yellow and you can make those places in repeat lists " "
    for i in range(5):
        if(repeat_guess_list[i] != " "):
            if(repeat_guess_list[i] in repeat_secret_list):
                color[i] = "yellow"
                repeat_secret_list[repeat_secret_list.index(repeat_guess_list[i])] = " "
                repeat_guess_list[i] = " "
    return color

def known_word(clues):
    """Takes a list of guesses taken and clues recieved in tuples as the element. It returns a string what we know about the secret with the green hints"""
    clues = dict(clues)
    list_output = ['_'] * 5
    str_output = ""
    #For each dictionary pair in clues add if we know that the letter is green to a list
    for i in clues:
        k = 0
        for j in clues[i]:
            if(k < 5):
                guess = i
                if(j == "yellow" or j == "grey"):
                    k += 1
                else:
                    list_output[k] = guess[k]
                    k += 1
    #Make a string with the _ or letter known and return it
    for i in range(len(list_output)):
        str_output = str_output + list_output[i]
    return str_output

def no_letters(clues):
    """Takes a list of guesses taken clues recieved. It returns a string"""
    clues = dict(clues)
    list_grey_output = []
    list_yellow_green_output = []
    str_grey_output = ""
    #Go throgh each clue and if a letter is grey and not already in the lists append it
    for i in clues:
        k = 0
        for j in clues[i]:
                guess = i
                if(j == "grey" and guess[k] not in list_grey_output and guess[k] not in list_yellow_green_output):
                    list_grey_output.append(guess[k])
                    k = k + 1
                else:
                    list_yellow_green_output.append(guess[k])
                    k = k + 1
    list_grey_output = sorted(list_grey_output)
    #Make a string with the list we have of the known grey letters then return it
    for i in range(len(list_grey_output)):
        str_grey_output = str_grey_output + list_grey_output[i]
    return str_grey_output

def yes_letters(clues):
    """Takes a list of guesses taken clues recieved. It returns a string"""
    clues = dict(clues)
    list_grey_output = []
    list_yellow_green_output = []
    str_yellow_green_output = ""
    #Go throgh each clue and if a letter is yellow or green and not already in the lists append it
    for i in clues:
        k = 0
        for j in clues[i]:
                guess = i
                if(j == "yellow" or j == "green"):
                    if(guess[k] not in list_yellow_green_output and guess[k] not in list_grey_output):
                        list_yellow_green_output.append(guess[k])
                    k = k + 1
                else:
                    list_grey_output.append(guess[k])
                    k = k + 1
                
    list_yellow_green_output = sorted(list_yellow_green_output)
    #Make a string with the list we have of the known yelllow or green letters then return it
    for i in range(len(list_yellow_green_output)):
        str_yellow_green_output = str_yellow_green_output + list_yellow_green_output[i]
    return str_yellow_green_output

def game(secret):
    """Takes in a secret word and returns nothing"""
    guess_num = 0
    clues_list = []
    clues_done = []
    guess = ""
    #Print out the blank's we do not know anything yet
    print("Known:", known_word(clues_list))
    print("Green/Yellow Letters:", yes_letters(clues_list))
    print("Grey Letters:", no_letters(clues_list))

    #While the guess number is less than 6 times and guess does not equal secret
    while(guess_num <= 5 and guess != secret):
        guess = str(input("> ")).upper()
        if(len(guess) == 5):
            guess_num += 1
            if(guess != secret):
                #If the guess is not the secret append the guess to the clues and the clues to the list
                clues_done.insert(0, guess)
                clues_list.append((guess, check_word(secret, guess)))
                #Go through word and each letter in the clues guessed and print out the letter with the color
                for i in clues_done[::-1]:
                    x = 0
                    for j in i:
                        if(check_word(secret, i)[x] == "yellow"):
                            display_utility.yellow(j)
                        elif(check_word(secret, i)[x] == "green"):
                            display_utility.green(j)
                        else:
                            display_utility.grey(j)
                        x += 1
                    print()
                #Print out the known information so far with letters
                print("Known:", known_word(clues_list))
                print("Green/Yellow Letters:", yes_letters(clues_list))
                print("Grey Letters:", no_letters(clues_list))
        else:
            print("Not a word. Try again")
    #If the guess is the secret print out each guess with colors and then the answer
    if(guess == secret):
        clues_done.insert(0, guess)
        for i in clues_done[::-1]:
            x = 0
            for j in i:
                if(check_word(secret, i)[x] == "green"):
                    display_utility.green(j)
                elif(check_word(secret, i)[x] == "yellow"):
                    display_utility.yellow(j)
                else:
                    display_utility.grey(j)
                x += 1
            print()
        print("Answer:", guess)


#START THE GAME HERE WITH WHATEVER WORD YOU WANT
game("WORDY")