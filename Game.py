
import random
def select_word():
    word_list = ['snake', 'cherry', 'elephant', 'banana', 'tiger', 'orange']  # Predefined list of words
    return random.choice(word_list)


def play_game():
    attempts = 3
    play_again = "yes"

    print("Welcome to Mystery Word!")

    while play_again.lower() == "yes":
        word = select_word()
        clues = [
            f"The word has {len(word)} letters.",
            f"The first letter is '{word[0]}'.",
            f"The word rhymes with '{word[::-1]}'."
        ]

        print("\nClues:")
        for i in clues:
            print(f"- {i}")
            # print("- ", i)

        print(f"\nAttempts left: {attempts}")

        while attempts > 0:
            guess = input("Guess the word: ")
            if guess.lower() == word:
                print(f"Congratulations! You guessed the word '{word}'! Well done!")
                break
            else:
                attempts -= 1
                if attempts > 0:
                    print("Incorrect guess. Try again.")
                    print(f"Attempts left: {attempts}")
                else:
                    print(f"Sorry, you ran out of attempts. The word was '{word}'.")

        play_again = input("\nDo you want to play again? (yes/no): ")

    print("\nThanks for playing Mystery Word! Goodbye.")

play_game()
