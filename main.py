import random

red_dot = chr(128308)
exit = False
user_points = 0
computer_points = 0
while exit == False:
    options = ["rock", "paper", "scissors"]
    user_input = input(
        "\n\033[93m>\033[0m Choose Rock, Paper, Scissors or Exit: ")
    computer_input = random.choice(options)

    if user_input.lower() == "exit":
        print(
            f"\nYour Score is \033[95m{user_points}\033[0m, Computer's Score is \033[95m{computer_points}\033[0m")
        print("\nProgram ended\n")
        exit = True

    elif user_input.lower() == "rock":
        print("\nYou chose Rock ✊")
        if computer_input == "rock":
            print("Computer chose Rock ✊")
            print("It's a tie")
        elif computer_input == "paper":
            print("Computer chose Paper ✋")
            print("Computer wins")
            computer_points = + 1
        elif computer_input == "scissors":
            print("Computer chose scissors ✌")
            print("You win")
            user_points = + 1

    elif user_input.lower() == "paper":
        print("\nYou chose Paper ✋")
        if computer_input == "rock":
            print("Computer chose Rock ✊")
            print("You win")
            user_points += 1
        elif computer_input == "paper":
            print("Computer chose Paper ✋")
            print("It's a tie")
        elif computer_input == "scissors":
            print("Computer chose scissors ✌")
            print("Computer wins")
            computer_points += 1

    elif user_input.lower() == "scissors":
        print("\nYou chose scissors ✌")
        if computer_input == "rock":
            print("Computer chose Rock ✊")
            print("Computer win")
            computer_points += 1
        elif computer_input == "paper":
            print("Computer chose scissors ✌")
            print("You win")
            user_points += 1
        elif computer_input == "scissors":
            print("Computer chose scissors ✌")
            print("It's a tie")
    else:
        print("\n" + red_dot + "\033[91m Enter a valid choice.\033[0m")
