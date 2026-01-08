import random

def game():
    print("Welcome to Stone, Paper, Scissors Game 🎮")
    print("Enter your choice: stone, paper, or scissor")

    user_choice = input("Your choice: ").lower()
    choices = ["stone", "paper", "scissor"]

    if user_choice not in choices:
        print("Invalid choice! Please choose stone, paper, or scissor.")
        return

    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a Draw ")
    elif (
        (user_choice == "stone" and computer_choice == "scissor") or
        (user_choice == "paper" and computer_choice == "stone") or
        (user_choice == "scissor" and computer_choice == "paper")
    ):
        print("You Win 🎉")
    else:
        print("You Lose 😢")

# Run the game
game()
