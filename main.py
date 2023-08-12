import os

from random_word import RandomWords

global difficulty
difficulty = 0
def initProj():
    print("Lets hang the python!! Choose a difficulty: 1, 2, or 3.")


def getDiff():
    global difficulty
    difficulty = int(input("Selected Difficulty: "))


initProj()


while True:
    if difficulty < 1 or difficulty > 3:
        print("That option is unavailable. Try again.")
        getDiff()
    else:
        print("You have selected difficulty level " + str(difficulty))
        break

global error_count
error_count = 0

global wordToGuess
wordToGuess = RandomWords().get_random_word()

global char_positions
char_positions = []

global guessed
guessed = []

global endGameCondition
endGameCondition = False


def drawSnake(stage):
    snakelist = [
        [
            ["                                                               "],
            ["                                                               "],
            ["                                                               "],
            ["                                                               "],
            ["                                                               "],
            ["                                                               "],
            ["                                                               "],
            ["                                                               "],
            ["                                                               "],
            ["                                                               "],
            ["                                                               "],
            ["                                                               "],
            ["                                                               "],
            ["                                                               "],
            ["                                                               "],
            ["                                                               "]
        ],
        [
            ["   Y                                                           "],
            ["  .-^-.                                                        "],
            [" /     \\                                                      "],
            ["()     ()                                                      "],
            [" \\_   _/                                                      "],
            ["                                                               "],
            ["                                                               "],
            ["                                                               "],
            ["                                                               "],
            ["                                                               "],
            ["                                                               "],
            ["                                                               "],
            ["                                                               "],
            ["                                                               "],
            ["                                                               "],
            ["                                                               "]
        ],
        [
            ["   Y                                                           "],
            ["  .-^-.                                                        "],
            [" /     \\                                                      "],
            ["()     ()                                                      "],
            [" \\_   _/                                                      "],
            ["   | |                                                         "],
            ["   | |    /  /                                                 "],
            ["   \\ \\_ _/  /                                                "],
            ["    \\_ _ _.'                                                  "],
            ["                                                               "],
            ["                                                               "],
            ["                                                               "],
            ["                                                               "],
            ["                                                               "],
            ["                                                               "],
            ["                                                               "]
        ],
        [
            ["   Y                                                           "],
            ["  .-^-.                                                        "],
            [" /     \\      .- ~ ~ -.                                       "],
            ["()     ()    /   _ _   `.                                      "],
            [" \\_   _/    /  /     \\   \\                                  "],
            ["   | |     /  /                                                "],
            ["   | |    /  /                                                 "],
            ["   \\ \\_ _/  /                                                "],
            ["    \\_ _ _.'                                                  "],
            ["                                                               "],
            ["                                                               "],
            ["                                                               "],
            ["                                                               "],
            ["                                                               "],
            ["                                                               "],
            ["                                                               "]
        ],
        [
            ["   Y                                                           "],
            ["  .-^-.                                                        "],
            [" /     \\      .- ~ ~ -.                                       "],
            ["()     ()    /   _ _   `.                                      "],
            [" \\_   _/    /  /     \\   \\                                  "],
            ["   | |     /  /       \\   \\                                  "],
            ["   | |    /  /         )   )                                   "],
            ["   \\ \\_ _/  /         /   /                                  "],
            ["    \\_ _ _.'         /   /                                    "],
            ["                    /   /                                      "],
            ["                   /   /                                       "],
            ["                                                               "],
            ["                                                               "],
            ["                                                               "],
            ["                                                               "],
            ["                                                               "]
        ],
        [
            ["   Y                                                           "],
            ["  .-^-.                                                        "],
            [" /     \\      .- ~ ~ -.                                       "],
            ["()     ()    /   _ _   `.                                      "],
            [" \\_   _/    /  /     \\   \\                                  "],
            ["   | |     /  /       \\   \\                                  "],
            ["   | |    /  /         )   )                                   "],
            ["   \\ \\_ _/  /         /   /                                  "],
            ["    \\_ _ _.'         /   /                                    "],
            ["                    /   /                                      "],
            ["                   /   /                                       "],
            ["                  /   /                                        "],
            ["                 (   (                                         "],
            ["                  `.  `.                                       "],
            ["                    `.   ~                                     "],
            ["                       ~                                       "]
        ],
        [
            ["   Y                                                           "],
            ["  .-^-.                                                        "],
            [" /     \\      .- ~ ~ -.                                       "],
            ["()     ()    /   _ _   `.                                      "],
            [" \\_   _/    /  /     \\   \\                                  "],
            ["   | |     /  /       \\   \\                                  "],
            ["   | |    /  /         )   )                                   "],
            ["   \\ \\_ _/  /         /   /                                  "],
            ["    \\_ _ _.'         /   /                                    "],
            ["                    /   /                                      "],
            ["                   /   /                                       "],
            ["                  /   /                                        "],
            ["                 (   (                                         "],
            ["                  `.  `.                                       "],
            ["                    `.   ~ - - - -                             "],
            ["                       ~ . _ _ _ _ .                           "]
        ],
        [
            ["   Y                                                           "],
            ["  .-^-.                                                        "],
            [" /     \\      .- ~ ~ -.                                       "],
            ["()     ()    /   _ _   `.                                      "],
            [" \\_   _/    /  /     \\   \\                                  "],
            ["   | |     /  /       \\   \\                                  "],
            ["   | |    /  /         )   )                                   "],
            ["   \\ \\_ _/  /         /   /                                  "],
            ["    \\_ _ _.'         /   /                                    "],
            ["                    /   /                                      "],
            ["                   /   /               \\  \\                  "],
            ["                  /   /                 )  )                   "],
            ["                 (   (                 /  /                    "],
            ["                  `.  `.             .'  /                     "],
            ["                    `.   ~ - - - - ~   .'                      "],
            ["                       ~ . _ _ _ _ . ~                         "]
        ],
        [
            ["   Y                                                        "],
            ["  .-^-.                                                     "],
            [" /     \\      .- ~ ~ -.                                     "],
            ["()     ()    /   _ _   `.                                   "],
            [" \\_   _/    /  /     \\   \\                                  "],
            ["   | |     /  /       \\   \\                                 "],
            ["   | |    /  /         )   )           /  /                 "],
            ["   \\ \\_ _/  /         /   /           /  /                  "],
            ["    \\_ _ _.'         /   /           (  (                   "],
            ["                    /   /             \\  \\                  "],
            ["                   /   /               \\  \\                 "],
            ["                  /   /                 )  )                "],
            ["                 (   (                 /  /                 "],
            ["                  `.  `.             .'  /                  "],
            ["                    `.   ~ - - - - ~   .'                   "],
            ["                       ~ . _ _ _ _ . ~                      "]
        ],
        [
            ["   Y                                                        "],
            ["  .-^-.                                                     "],
            [" /     \\      .- ~ ~ -.                                     "],
            ["()     ()    /   _ _   `.                     _ _ _         "],
            [" \\_   _/    /  /     \\   \\                . ~  _ _          "],
            ["   | |     /  /       \\   \\             .' .~               "],
            ["   | |    /  /         )   )           /  /                 "],
            ["   \\ \\_ _/  /         /   /           /  /                  "],
            ["    \\_ _ _.'         /   /           (  (                   "],
            ["                    /   /             \\  \\                  "],
            ["                   /   /               \\  \\                 "],
            ["                  /   /                 )  )                "],
            ["                 (   (                 /  /                 "],
            ["                  `.  `.             .'  /                  "],
            ["                    `.   ~ - - - - ~   .'                   "],
            ["                       ~ . _ _ _ _ . ~                      "]
        ],
        [
            ["   Y                                                        "],
            ["  .-^-.                                                     "],
            [" /     \\      .- ~ ~ -.                                     "],
            ["()     ()    /   _ _   `.                     _ _ _         "],
            [" \\_   _/    /  /     \\   \\                . ~  _ _  ~ .     "],
            ["   | |     /  /       \\   \\             .' .~       ~-. `.  "],
            ["   | |    /  /         )   )           /  /             `.`."],
            ["   \\ \\_ _/  /         /   /           /  /                `'"],
            ["    \\_ _ _.'         /   /           (  (                  "],
            ["                    /   /             \\  \\                  "],
            ["                   /   /               \\  \\                 "],
            ["                  /   /                 )  )                "],
            ["                 (   (                 /  /                 "],
            ["                  `.  `.             .'  /                  "],
            ["                    `.   ~ - - - - ~   .'                   "],
            ["                       ~ . _ _ _ _ . ~                      "]
        ],
        [
            ["   Y                                                        "],
            ["  .-^-.                                                     "],
            [" /     \\      .- ~ ~ -.                                     "],
            ["X       X    /   _ _   `.                     _ _ _         "],
            [" \\_   _/    /  /     \\   \\                . ~  _ _  ~ .     "],
            ["   | |     /  /       \\   \\             .' .~       ~-. `.  "],
            ["   | |    /  /         )   )           /  /             `.`."],
            ["   \\ \\_ _/  /         /   /           /  /                `'"],
            ["    \\_ _ _.'         /   /           (  (                  "],
            ["                    /   /             \\  \\                  "],
            ["                   /   /               \\  \\                 "],
            ["                  /   /                 )  )                "],
            ["                 (   (                 /  /                 "],
            ["                  `.  `.             .'  /                  "],
            ["                    `.   ~ - - - - ~   .'                   "],
            ["                       ~ . _ _ _ _ . ~                      "]
        ],
        [
            ["   Y                                                        "],
            ["  .-^-.                                                     "],
            [" /     \\      .- ~ ~ -.     DEAD                            "],
            ["X       X    /   _ _   `.                     _ _ _         "],
            [" \\_   _/    /  /     \\   \\                . ~  _ _  ~ .     "],
            ["   | |     /  /       \\   \\             .' .~       ~-. `.  "],
            ["   | |    /  /         )   )           /  /             `.`."],
            ["   \\ \\_ _/  /         /   /           /  /                `'"],
            ["    \\_ _ _.'         /   /           (  (                  "],
            ["                    /   /             \\  \\                  "],
            ["                   /   /               \\  \\                 "],
            ["                  /   /                 )  )                "],
            ["                 (   (                 /  /                 "],
            ["                  `.  `.             .'  /                  "],
            ["                    `.   ~ - - - - ~   .'                   "],
            ["                       ~ . _ _ _ _ . ~                      "]
        ]
    ]
    for element in range(0,15):
        print(*snakelist[stage][element])
        

def gameCycle():
    global error_count

    print(wordToGuess)
    drawSnake(error_count)
    print("MAKE A GUESS: ", end="")
    for element in range(0, len(wordToGuess)):
        if element in char_positions:
            print(wordToGuess[element:element+1], end=" ")
        else:
            print("_", end=" "),
    print()
    print("You Have Guessed: ", end="")
    for element in guessed:
        print(element, end=" ")
    print()
    u_input = input("Your Guess: ")

    counter = 0  # tracks index off guess in word
    correct = False

    if len(u_input) == 1:
        if u_input not in guessed:
            guessed.append(u_input)
        for element in wordToGuess:
            if element == u_input:
                if counter not in char_positions:
                    char_positions.append(counter)
                    correct = True
            counter += 1
    elif len(u_input) > 1:
        if u_input in wordToGuess and len(u_input) == len(wordToGuess):
            for element in range(0, len(wordToGuess)):
                if element not in char_positions:
                    char_positions.append(element)
            correct = True

    if not correct:
        error_count += 1 * difficulty


while (not len(char_positions) == len(wordToGuess)) and not(error_count == 12):
    gameCycle()
    os.system('cls')

if len(char_positions) == len(wordToGuess):
    endGameCondition = True

if endGameCondition:
    print("YOU WIN. YAYY.")
else:
    drawSnake(error_count)
    print("YOU HAVE HUNG THE PYTHON. YOU LOSE BOZO.")
print(wordToGuess + " was the word.")
