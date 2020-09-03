import random
from words import word_list

def get_word():
    word = random.choice(word_list)
    return word.upper()

def play(word):
    word_completion = "-" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Let's Play Hangman")
    print(display_hangman(tries))
    print(word_completion,"\n")
    while not guessed and tries>0:
        guess = input("Guess a letter or a word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f"You have guessed the letter '{guess}'")
            elif guess not in word:
                print(f"'{guess}' is not present in the word")
                tries -= 1
                print(f"tries remaining {tries}")
                guessed_letters.append(guess)
            else:
                print(f"Great!!! '{guess}' is present in the word")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
            if "-" not in word_completion:
                guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print(f"You have guessed the word '{guess}'")
            elif guess not in word:
                print(f"'{guess}' is not present")
                tries -= 1
                print(f"tries remaining {tries}")
                guessed_letters.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Invalid Guess")
        print(display_hangman(tries))
        print(word_completion,"\n")
    
    if guessed:
        print("Woohoo!!! You have guessed the word correctly!")
    else:
        print(f"Oops!!!, You ran out of tries. The word was {word}. Better Luck next time")

def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   ________
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   ________
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   ________
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   ________
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   ________
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   ________
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   ________
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]

def main():
    word = get_word()
    play(word)
    while input("Play Again? (Y/N) ").upper() == 'Y':
        word = get_word()
        play(word)

if __name__ == "__main__":
    main()