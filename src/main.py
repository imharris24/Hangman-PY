import random
import os

# list of random words
wordList = ['cat', 'cloud', 'cricket', 'football', 'dog', 'rain', 'devil', 'angel', 'feather', 'happy', 'sad']

# hangman ASCII art
hangmanASCII = ['\n\t   +---+\n\t   |   |\n\t       |\n\t       |\n\t       |\n\t       |\n\t========', '\n\t   +---+\n\t   |   |\n\t   o   |\n\t       |\n\t       |\n\t       |\n\t========', '\n\t   +---+\n\t   |   |\n\t   o   |\n\t   |   |\n\t       |\n\t       |\n\t========', '\n\t   +---+\n\t   |   |\n\t   o   |\n\t  /|   |\n\t       |\n\t       |\n\t========', '\n\t   +---+\n\t   |   |\n\t   o   |\n\t  /|\\  |\n\t       |\n\t       |\n\t========', '\n\t   +---+\n\t   |   |\n\t   o   |\n\t  /|\\  |\n\t  /    |\n\t       |\n\t========', '\n\t   +---+\n\t   |   |\n\t   o   |\n\t  /|\\  |\n\t  / \\  |\n\t       |\n\t========']

# function that returns a random word
def returnRandomWord():
    return random.choice(wordList)

# function that runs a single session of hangman
def playHangman(word, life, key):
    os.system('cls')
    print('\n\tHangman\n')

    # condition if player loses
    if life == 6:
        os.system('cls')
        print('\nGame Over\n')
        print('press enter key to start again')
        input()
        return True

    # condition if player wins
    if len(key) == 0:
        os.system('cls')
        print('\nYou WIN!\n')
        print('press enter key to start again')
        input()
        return True

    # if word is still incomplete

    print(hangmanASCII[life])

    # print word with encryption
    print('Word: ', end='')
    for x in word:
        if x in key:
            print('_', end='')
        else:
            print(x, end='')

    # take player input
    alpha = input('\n\nINPUT: ')[0]

    # if input exists in word, discard it from key
    # else hangman loses a life
    if alpha in key:
        key.discard(alpha)
    else:
        life = life + 1

    # recur until word is complete or game is over
    playHangman(word, life, key)


# main

while True:
    word = returnRandomWord()
    lifes = 0
    key = set(word)
    while True:
        exec = playHangman(word, lifes, key)
        if not exec:
            break
