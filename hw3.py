import random

name = input("Please enter your name: ").upper()
print("Welcome {}! ".format(name))
print("Let's play Hangman!")

words = [ "isolation", "transmission", "quarantine", "bat", "virus", "asymptomatic", "contagion",
         "vaccine", "distant", "coronavirus ", "mask", "pandemic", "pain"]

word = random.choice(words)
tries = 7
letters = []
x = len(word)
z = list('_'* x)
print(' '.join(z), end='\n')
while tries > 0:
    guess = input("Please guess a letter: ")
    if guess in letters:
        print("You have already guessed that letter! Please guess a different letter: ")
        continue

    elif len(guess) > 1:
        print("Please guess just a letter!")
        continue

    elif guess not in word:
        tries -= 1
        print(guess,"is not in the word. You have {} guesses left.".format(tries))

    else:
        for i in range(len(word)):
            if guess == word[i]:
                print("Right guess!")
                z[i] = guess
                letters.append(guess)
        print(' '.join(z), end='\n')

    answer = input("Do you wanna guess the word? ['y'/'n'] : ")

    if answer == "y":
        guess = input("Word is : ")
        if guess == word:
            print("Congrats! You guessed correctly :)")
            break
        else:
            tries -= 1
            print("Wrong!")
            print(" Try Again! You have {} guesses left.".format(tries))


    if tries == 0:
        print("You don't have guesses left. You lost :( ")
        break