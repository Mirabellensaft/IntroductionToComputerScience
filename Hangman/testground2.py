def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    SecretWordToList = (list(secretWord))

    for item in SecretWordToList:
        if item in lettersGuessed:
            print (True)
        else:
            print (False)
            break
WordToBeGuessed = 'apple'
LettersAlready = ['l', 'x', 'k', 'p', 'e']

isWordGuessed(WordToBeGuessed, LettersAlready)
