import os

from random_word import RandomWords


def initProj():
    print("Lets hang the python!! Choose a difficulty: 1, 2, or 3.")


def getDiff():
    global difficulty
    difficulty = 0
    difficulty = int(input("Selected Difficulty: "))


initProj()

"""
while True:
    if difficulty < 1 or difficulty > 3:
        print("That option is unavailable. Try again.")
        getDiff()
    else:
        print("You have selected difficulty level " + str(difficulty))
        break
"""

global wordToGuess
wordToGuess = RandomWords().get_random_word()

global char_positions
char_positions = []

def drawSnake(stages, current_stage):

"""
   Y
  .-^-.
 /     \      .- ~ ~ -.
()     ()    /   _ _   `.                     _ _ _
 \_   _/    /  /     \   \                . ~  _ _  ~ .
   | |     /  /       \   \             .' .~       ~-. `.
   | |    /  /         )   )           /  /             `.`.
   \ \_ _/  /         /   /           /  /                `'
    \_ _ _.'         /   /           (  (
                    /   /             \  \
                   /   /               \  \
                  /   /                 )  )
                 (   (                 /  /
                  `.  `.             .'  /
                    `.   ~ - - - - ~   .'
                       ~ . _ _ _ _ . ~





   Y
  .-^-.
 /     \      .- ~ ~ -.
X       X    /   _ _   `.                     _ _ _
 \_   _/    /  /     \   \                . ~  _ _  ~ .
   | |     /  /       \   \             .' .~       ~-. `.
   | |    /  /         )   )           /  /             `.`.
   \ \_ _/  /         /   /           /  /                `'
    \_ _ _.'         /   /           (  (
                    /   /             \  \
                   /   /               \  \
                  /   /                 )  )
                 (   (                 /  /
                  `.  `.             .'  /
                    `.   ~ - - - - ~   .'
                       ~ . _ _ _ _ . ~
"""

def gameCycle():
    print("MAKE A GUESS: ", end="")
    for element in range(0, len(wordToGuess)):
        if element in char_positions:
            print(wordToGuess[element:element+1], end="")
        else:
            print("_", end=""),
    print()
    u_input = input("Your Guess: ")

    counter = 0
    if len(u_input) == 1:
        for element in wordToGuess:
            if element == u_input and counter not in char_positions:
                char_positions.append(counter)
            counter += 1

while not len(char_positions) == len(wordToGuess):
    gameCycle()
    os.system('cls')
