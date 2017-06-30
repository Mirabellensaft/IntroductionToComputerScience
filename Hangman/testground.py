def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # removes duplicates from the list of characters contained in the secretWord
    def remove_duplicates(characters):
        LettersInSecretWord = []
        seen = set()
        for character in characters:
            # If value has not been encountered yet,
            # ... add it to both list and set.
            if character not in seen:
                LettersInSecretWord.append(character)
                seen.add(character)
        print (LettersInSecretWord)
        return LettersInSecretWord

    SecretWordToList = (list(secretWord))

    CharactersInSecretWord = remove_duplicates(SecretWordToList)
    # compares both character lists. If they are the same, True is returned


    for item in CharactersInSecretWord:
        if item in lettersGuessed:
            print (True)
        else:
            print (False)


WordToBeGuessed = 'apple'
LettersAlready = ['a', 'x', 'l', 'p', 'e']

isWordGuessed(WordToBeGuessed, LettersAlready)
