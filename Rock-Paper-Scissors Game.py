import random

def determine_winner(user_choice, computer_choice):
    """Determine the winner based on game rules"""
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

def play_game():
    print("\nRock-Paper-Scissors Game")
    print("------------------------")
    print("Game Rules:")
    print("- Rock beats scissors")
    print("- Scissors beat paper")
    print("- Paper beats rock")
    
    choices = ["rock", "paper", "scissors"]
    user_score = 0
    computer_score = 0
    
    while True:
        # User input with validation
        while True:
            user_choice = input("\nChoose rock, paper, or scissors (or 'quit' to exit): ").lower()
            if user_choice in choices + ["quit"]:
                break
            print("Invalid choice. Please try again.")
        
        if user_choice == "quit":
            break
        
        # Computer selection
        computer_choice = random.choice(choices)
        print(f"\nYour choice: {user_choice}")
        print(f"Computer's choice: {computer_choice}")
        
        # Determine winner
        result = determine_winner(user_choice, computer_choice)
        
        # Update scores and display result
        if result == "user":
            user_score += 1
            print("You win!")
        elif result == "computer":
            computer_score += 1
            print("Computer wins!")
        else:
            print("It's a tie!")
        
        # Display current score
        print(f"\nCurrent Score - You: {user_score} | Computer: {computer_score}")
    
    # Final results when quitting
    print("\nFinal Results:")
    print(f"You: {user_score} | Computer: {computer_score}")
    if user_score > computer_score:
        print("Congratulations! You won the game!")
    elif computer_score > user_score:
        print("Computer won the game. Better luck next time!")
    else:
        print("The game ended in a tie!")

if __name__ == "__main__":
    play_game()