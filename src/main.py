import random

# list of random words
wordList = ['cat', 'cloud', 'cricket', 'football', 'dog', 'rain', 'devil', 'angel', 'feather', 'happy', 'sad']
# function that returns a random word
def returnRandomWord():
    return random.choice(wordList)


# main
print('\tHangman')
