from random import randint  # Do not delete this line


def displayIntro():
    fileName = 'hangman-ascii.txt'
    file = open(fileName, 'r')
    displayList = file.read().splitlines()
    for intro in range(1, 24):
        print(displayList[intro])


def displayEnd(result):
    fileName = 'hangman-ascii.txt'
    file = open(fileName, 'r')
    displayList = file.read().splitlines()
    if result:
        for ending in range(190, 203):
            print(displayList[ending])
    else:
        for ending in range(99, 112):
            print(displayList[ending])


def displayHangman(state):
    fileName = 'hangman-ascii.txt'
    file = open(fileName, 'r')
    displayList = file.read().splitlines()
    if state == 5:
        for index in range(24, 33):
            print(displayList[index])
    if state == 4:
        for index in range(37, 46):
            print(displayList[index])
    if state == 3:
        for index in range(50, 59):
            print(displayList[index])
    if state == 2:
        for index in range(63, 72):
            print(displayList[index])
    if state == 1:
        for index in range(76, 85):
            print(displayList[index])
    if state == 0:
        for index in range(89, 98):
            print(displayList[index])


def getWord():
    fileName = 'hangman-words.txt'
    file = open(fileName, 'r')
    listOfWords = file.read().splitlines()
    theOne = randint(0, 853)
    return listOfWords[theOne]


def valid(c):
    if len(c)==1 and 97 <= ord(c) and ord(c) <= 122  :
        return True
    else:
        return False


def play():
    word=getWord()
    state = 5
    guess = ''
    for count in range(0, len(word)):
        guess += '_'
    while state != 0:
        displayHangman(state)
        print("Guess the word: " + guess)
        print("Enter the letter: ")
        inp = input()
        while not valid(inp):
            print("Please write one lower case letter: ")
            inp1 = input()
            inp = inp1
        if inp in word:
            newGuess = ''
            for index in range(0, len(word)):
                if guess[index] != '_':
                    newGuess += guess[index]
                elif word[index] == inp:
                    newGuess += inp
                else:
                    newGuess += '_'
            guess = newGuess
        else:
            state -= 1
        if '_' not in guess:
            print("Hidden word was: " + word)
            return True
    print("Hidden word was: " + word)
    return False


def hangman():
    while True:
        displayIntro()
        result = play()
        displayEnd(result)
        print("Do you want to play again? (yes/no)")
        ans = input()
        if ans == 'yes':
            continue
        else:
            break


if __name__ == "__main__":
    hangman()