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

print("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.")
rock_move = 0
paper_move = 1
scissors_move = 2

losing_moves_for_computer = [scissors_move, rock_move, paper_move] 

def printMove(move):
    if move == rock_move:
        print(rock)
    elif move == paper_move:
        print(paper)
    else: 
        print(scissors)

def getMoveName(move: int):
    if move == rock_move:
        return "Rock"
    elif move == paper_move:
        return "Paper"
    else: 
        return "Scissors"

player_choice = int(input())
printMove(player_choice)

print("Computer Choose")
random_computer_choice = random.randint(0, 2)
printMove(random_computer_choice)

# win / lose logic

if player_choice == random_computer_choice:
    print("Tie!")
else:
    computer_has_losing_move = random_computer_choice == losing_moves_for_computer[player_choice]
    if computer_has_losing_move:
        print("You Win!")    
        print(f"{getMoveName(player_choice)} beats {getMoveName(random_computer_choice)}!")
    else:
        print("You Lose!")
        print(f"{getMoveName(player_choice)} loses to {getMoveName(random_computer_choice)}!")

