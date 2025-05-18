import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''

rock_paper_scissors = [rock, paper, scissors]

users_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for sciccors."))
if users_choice > 3 or users_choice < 0 :
    print("Please choose an option 0, 1, or 2.")
else:
    print(rock_paper_scissors[users_choice])

    # We want the computer to randomly choose a number from 0 to 2
    computer_choice = random.randint(0, len(rock_paper_scissors) - 1)
    print("Computer chose:\n ")
    print(rock_paper_scissors[computer_choice])

    if users_choice == 0:
        if computer_choice == 1:
            print("You lost!")
        elif computer_choice == 2:
            print("You won!")
        else:
            print("It's a draw!")

    elif users_choice == 1:
        if computer_choice == 0:
            print("You won!")
        elif computer_choice == 2:
            print("You lost!")
        else:
            print("It's a draw!")

    elif users_choice == 2:
        if computer_choice == 0:
            print("You lost!")
        elif computer_choice == 1:
            print("You won!")
        else:
            print("It's a draw!")
