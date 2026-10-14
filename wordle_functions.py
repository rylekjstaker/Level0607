# import random and create secret words list
import random

secret_words = ["crane", "plant", "slate", "mouse", "brick",
"chair", "drink", "flame", "ghost", "jumpy",
"light", "ocean", "pride", "query", "robin",
"shark", "tiger", "uncle", "voice", "world",
"yacht", "zebra", "blast", "frost", "house"]

#custom function to select a random word from the list

def choose_word():
    return random.choice(secret_words)

# creating get-guess to get the players guess

def get_guess(previous_guesses):
    while True:
        guess = input("Enter a five-letter word: ").lower()
        if len(guess) != 5:
            print("Your guess must be exactly 5 letters.")
        elif guess in previous_guesses:
            print("You already guessed that word. Try again.")
        else:
            return guess

# Custom function to compare player guess to secret word

def evaluate_guess(guess, secret_word):
    evaluation = []
    for i in range(0,5,1):
        if secret_word[i] == guess[i]:
            evaluation.append("G")
        elif guess[i] in secret_word:
            evaluation.append("Y")
        else:
            evaluation.append("-") 
    return evaluation
        
# Custom function to display the guesses and evaluation
def display_guess(guess, evaluation):
    print(f"\nGuess:    {guess[0].upper()} {guess[1].upper()} {guess[2].upper()} {guess[3].upper()} {guess[4].upper()}")
    print(f"Feedback: {evaluation[0]} {evaluation[1]} {evaluation[2]} {evaluation[3]} {evaluation[4]}")

# Custom function to verify if the player has won
def has_won(guess, secret_word):
    if guess == secret_word:
        return True
    else:
        return False

