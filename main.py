import random  
import re     

# Setting the number of tries allowed
tries = 5

# All possible answers
listOfwords = ['amber', 'apple', 'argue', 'beach', 'bread', 'brush', 'chair', 'chest', 'chili', 'clock', 'cloud', 'coach', 'dance', 'dated', 'diner', 'drink', 'early', 'email', 'fence', 'fleet', 'flirt', 'floor', 'fresh', 'frost', 'glare', 'glove', 'grass', 'greet', 'grime', 'happy', 'heart', 'house', 'humor', 'index', 'laugh', 'light', 'lodge', 'lunch', 'mango', 'march', 'metal', 'onion', 'paint', 'peach', 'plank', 'plate', 'plum', 'proud', 'quiet', 'river', 'roast', 'salad', 'scale', 'shoes', 'skate', 'slide', 'smile', 'snake', 'snore', 'sound', 'space', 'spicy', 'spoon', 'stage', 'steam', 'stick', 'stone', 'straw', 'table', 'taste', 'tiger', 'toast', 'trail', 'train', 'trash', 'uncle', 'voice', 'watch', 'water', 'wheel', 'woman', 'world', 'write', 'young', 'alarm', 'angel', 'armor', 'attic', 'bacon', 'baker', 'beach', 'blend', 'blink', 'brick', 'brush', 'cabin', 'candy', 'chair', 'charm', 'chase', 'cider', 'clamp', 'clean', 'clock', 'clown', 'crust', 'dance', 'diner', 'drift', 'drink', 'eagle', 'email', 'fence', 'flame', 'fleet', 'flirt', 'frown', 'glare', 'glove', 'grace', 'grass', 'greet', 'grime', 'heart', 'horse', 'humor', 'ivory', 'laugh', 'light', 'lodge', 'lunch', 'mango', 'march', 'metal', 'motor', 'onion', 'paint', 'peace', 'plank', 'plate', 'plum', 'proud', 'quiet', 'river', 'roast', 'salad', 'scale', 'shoes', 'skate', 'slide', 'smile', 'snake', 'snore', 'sound', 'space', 'spicy', 'spoon', 'stage', 'steam', 'stick', 'stone', 'straw', 'table', 'taste', 'tiger', 'toast', 'trail', 'train', 'trash', 'uncle', 'voice', 'watch', 'water', 'wheel', 'woman', 'world', 'write', 'young', 'alarm', 'angel', 'armor', 'attic', 'bacon', 'baker', 'beach', 'blend', 'blink', 'brick', 'brush', 'cabin', 'candy', 'chair', 'charm', 'chase', 'cider', 'clamp', 'clean', 'clock', 'clown', 'crust', 'dance', 'diner', 'drift', 'drink', 'eagle', 'email', 'fence', 'flame', 'fleet', 'flirt', 'frown', 'glare', 'glove', 'grace', 'grass', 'greet', 'grime', 'heart', 'horse', 'humor', 'ivory', 'laugh', 'light', 'lodge', 'lunch', 'mango', 'march', 'metal', 'motor', 'onion', 'paint', 'peace', 'plank', 'plate', 'plum', 'proud', 'quiet', 'river', 'roast', 'salad', 'scale', 'shoes', 'skate', 'slide', 'smile', 'snake', 'snore', 'sound', 'space', 'spicy', 'spoon', 'stage', 'steam', 'stick', 'stone', 'straw', 'table', 'taste', 'tiger', 'toast', 'trail', 'train', 'trash', 'uncle', 'voice', 'watch', 'water', 'wheel', 'woman', 'world', 'write', 'young', 'alarm', 'angel', 'armor', 'attic', 'bacon', 'baker', 'beach', 'blend', 'blink', 'brick', 'brush', 'cabin', 'candy', 'chair', 'charm', 'chase', 'cider', 'clamp', 'clean', 'clock', 'clown', 'crust', 'dance', 'diner', 'drift', 'drink', 'eagle', 'email', 'fence', 'flame', 'fleet', 'flirt', 'frown', 'glare', 'glove', 'grace', 'grass', 'greet', 'grime', 'heart', 'horse', 'humor', 'ivory', 'laugh', 'light', 'lodge', 'lunch', 'mango', 'march', 'metal', 'motor', 'onion', 'paint', 'peace', 'plank', 'plate', 'plum', 'proud', 'quiet', 'river', 'roast', 'salad', 'scale', 'shoes', 'skate', 'slide', 'smile', 'snake', 'snore', 'sound', 'space', 'spicy', 'spoon', 'stage', 'steam', 'stick', 'stone', 'straw', 'table', 'taste', 'tiger', 'toast', 'trail', 'train', 'trash', 'uncle', 'voice', 'watch', 'water', 'wheel', 'whisper', 'woman', 'world', 'write', 'young', 'alarm', 'angel', 'armor', 'attic', 'bacon', 'baker', 'beach', 'blend', 'blink', 'brick', 'brush', 'cabin', 'candy', 'chair', 'charm', 'chase', 'cider', 'clamp', 'clean', 'clock', 'clown', 'crust', 'dance', 'diner', 'drift', 'drink', 'eagle', 'email', 'fence', 'flame', 'fleet', 'flirt', 'frown', 'glare', 'glove', 'grace', 'grass', 'greet', 'grime', 'heart', 'horse', 'humor', 'ivory', 'laugh', 'light', 'lodge', 'lunch', 'mango', 'march', 'metal', 'motor', 'onion', 'paint', 'peace', 'plank', 'plate', 'proud', 'quiet', 'river', 'roast', 'salad', 'scale', 'shoes', 'skate', 'slide', 'smile']


# Lists to store user's guesses and the generated word
storedAnswers = []
answerDefined = []

# Variable to track if the user guessed the word correctly
gotitright = False

# Variable to track if the game has finished
finished = False

# Function to define the main game logic
def main():
    global gotitright, finished, tries, storedAnswers, answerDefined
    
    # Selecting a random word from the list
    generatedAnswer = random.choice(listOfwords)

    # Splitting the generated word into individual characters
    for i in generatedAnswer:
        answerDefined.append(i)

    # Welcoming the user and explaining the game
    print("Hello! Welcome to this fan-made version of Wordle using Python. In this game, you'll be given a 5-letter word to guess. You have 5 tries to guess the word. If a letter you guessed is in the correct position, it will be displayed. Remember, only lowercase 5-letter words are accepted. Good luck!")

    # Game loop
    while not finished:
        # Prompting the user for input
        answer = input(f"\nYou have {tries} tries left. Enter a 5-letter word: ")

        # Regular expression to check if the input follows the rules
        ruleset = re.compile(r'^[a-z]+$')

        # Validating the input
        if len(answer) == 5:
            if ruleset.match(answer):
                # Storing the user's input
                for char in answer:
                    storedAnswers.append(char)

                # Function to find common letters between the user's input and the generated word
                def intersection(storedAnswers, answerd):
                    lst3 = [value for value in storedAnswers if value in answerDefined]
                    return lst3

                # Checking if there are correct letters in the user's guess
                if len(intersection(storedAnswers, answerDefined)) > 0:
                    print(f"The letters you guessed correctly were: {set(intersection(storedAnswers, answerDefined))}")
                else:
                    print("There were no correct letters in your guess.")

                # Decreasing the number of tries
                tries -= 1

                # Checking if the user has used all tries
                if tries == 0:
                    finished = True

                # Clearing the stored user's answers
                storedAnswers.clear()

                # Checking if the user guessed the word correctly
                if answer == generatedAnswer:
                    finished = True
                    gotitright = True

            else:
                print("Please enter a lowercase 5-letter word only.")
                
        else:
            print("Please enter a lowercase 5-letter word only.")
    else:
        # Displaying the result of the game
        if gotitright:
            print("\nCongratulations! You guessed it right!")
            print(f"You got it in {tries} tries.")
        else:
            print(f"\nSorry, the answer was {generatedAnswer}. Better luck next time!")

# Executing the main function if the script is run directly
if __name__ == "__main__":
    main()
