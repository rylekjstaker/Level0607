# Level #0607 - Wordle
# IS 303 - Hilton
# Rylek Staker

#importing wordle functions file

import wordle_functions

play_again = "yes"

#Welcoming the user
print("Welcome to Mystery Wordle!")
print("\nGuess the five-letter word.")
print("\nG = correct letter and position")
print("Y = correct letter, wrong position")
print("- = letter is not in the word")



#game loop
while play_again == "yes":
    
    #selecting secret word and setting up game
    secret_word = wordle_functions.choose_word()
    previous_guesses = []
    num_attempts = 1
    won = False
            
    while num_attempts < 7 and won == False:

        print(f"\nAttempt {num_attempts} of 6")
        guess = wordle_functions.get_guess(previous_guesses)
        previous_guesses.append(guess)
    
    
        evaluation = wordle_functions.evaluate_guess(guess, secret_word)
        wordle_functions.display_guess(guess, evaluation)
        num_attempts += 1
    
        won = wordle_functions.has_won(guess, secret_word)
    
        if won == True:
            print("\nCongratulations! You solved the puzzle.")

    if won == False:
        print(f"The word was: {secret_word}")
        print("\nYou failed the game.")
        
    play_again = input("\nWould you like to play again? ").lower()

print("\nThanks for playing!")
    