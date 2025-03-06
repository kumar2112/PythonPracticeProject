# import random

# words = [
#          'rainbow', 'computer',  'science', 'programming',
#          'python' , 'mathematics', 'player', 'condition',
#          'reverse', 'water', 'board', 'geeks'
#         ]


# guessChance = 5

# randomWord = random.choice(words)

# guessCount =0

# print(f"Hi welcome to the game, This is a Word guessing game.\nYou got {guessChance} chances to guess the word. Let's start the game")

# name = input("What is your name? ")
# print("Good Luck ! ", name)
# print("\n\n")


# while guessCount < guessChance :
#    guessCount+=1
   
  
#    w = str(input("Enter Word!\n"))
   
#    if w in words :
#       print(f"Great! you guessed the correct word")
#       break
#    elif guessCount >= guessChance :
#       print(f"Oops! All {guessChance} chances are complete")
#       break
#    else :
#       print(f"You loose the chance {guessCount}\n")
#       print(f"Ooops! try again")
      


import random

name = input("What is your name? ")

print("Good Luck ! ", name)

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

word = random.choice(words)

print(word)

print("\nGuess the characters")

guesses = ''
turns = 12

while turns > 0:

    failed = 0

    for char in word:

        if char in guesses:
            print(char, end=" ")
        else:
            print("_")
            failed += 1

    if failed == 0:
        print("You Win")
        print("The word is: ", word)
        break

    print()
    guess = input("guess a character:")

    guesses += guess

    if guess not in word:

        turns -= 1
        print("Wrong")
        print("You have", + turns, 'more guesses')

        if turns == 0:
            print("You Loose")




