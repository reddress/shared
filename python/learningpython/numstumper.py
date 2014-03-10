"""
Bulls and Cows

After choosing the number of digits in the secret number, your task is to
guess the secret number. It will not have any repeating digits. The usual
number of digits is 3 or 4.

After each guess, the game will tell you how many digits match and are in
the right place (ones, tens, hundreds, etc. place,) and how many other digits
are in the secret number but in the wrong place.
"""

from random import randint

def generateSecret(digits):
    allDigits = list(range(0,10))
    secret = ""
    while digits > 0:
        secret += str(allDigits.pop(randint(0, len(allDigits) - 1)))
        digits -= 1
    return secret

def check(guess, secret):
    numberRight = 0
    numberInWrongPlace = 0

    # check number of digits in the right place
    updatedGuess = ""
    for i in range(len(guess)):
        if guess[i] == secret[i]:
            numberRight += 1
        else:
            updatedGuess += guess[i]
            
    # use remaining numbers to determine digits in wrong place
    numberInWrongPlace = len(set(updatedGuess).intersection(set(secret)))
    return (numberRight, numberInWrongPlace)

def getLength():
    try:
        desiredLength = int(input("Choose the number of digits (1-9): "))
        if 1 <= desiredLength <= 9:
            return desiredLength
        else:
            print("Choose a number from 1 to 9.")
            getLength()
    except ValueError:
        print("Please enter a number.")
        getLength()

def gameLoop(length, cheat):
    secret = generateSecret(length)
    numberRight = 0
    guesses = 0

    while numberRight < length:
        guess = input("Your guess (%s digits, q to quit)? " % length)
        if guess == "q":
            break
        
        if (guess.isdigit() and len(guess) == length and
            len(set(guess)) == length):
            numberRight, numberInWrongPlace = check(guess, secret)
            print("Number right (Bulls): %s, number in wrong place (Cows): %s" % (numberRight, numberInWrongPlace))
            if cheat:
                print("The secret number:", secret)
            print()
            guesses += 1
        else:
            print("Enter a %s-digit number without repeating digits." % length)

    if numberRight == length:
        print("You got it! Number of guesses: %s" % guesses)
    else:
        print("The secret number is:", secret)
    
def startGame(cheat=False):
    print("Bulls and Cows")
    print()
    gameLoop(getLength(), cheat=cheat)

startGame()
