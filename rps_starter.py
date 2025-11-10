from random import randint


rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
# Pick a random number from 1 to 3
num = randint(1,3)
computer_move =""

# Turn that random number into the computer's RPS move
if num==1:
    computer_move = "rock"
elif num==2:
    computer_move = "paper"
else:
    computer_move = "scissors"



# Ask a user to enter their move
move1=input("Enter your move:").lower()

# Print the rock, paper, or scissors ASCII art that corresponds to the player's move
print(f"Your move:{move1}")
if move1=="rock":
    print(rock)
elif move1=="scissors":
    print(scissors)
elif move1=="paper":
    print(paper)

# Print the rock, paper, or scissors ASCII art that corresponds to the computer's move

print(f"Compute choose: {computer_move}")
if computer_move=="rock":
    print(rock)
elif computer_move=="scissors":
    print(scissors)
elif computer_move=="paper":
    print(paper)

# Figure out who wins and print the result!
if move1=="rock" and computer_move=="paper":
    print("Computer wins!")
elif move1=="rock" and computer_move=="scissors":
    print("You wins!")
elif move1=="paper" and computer_move=="scissors":
    print("Computer wins!")
elif move1=="scissors" and computer_move=="rock":
    print("Computer wins!")
elif move1=="scissors" and computer_move=="paper":
    print("You wins")
elif move1=="paper" and computer_move=="rock":
    print("You wins")
elif move1==computer_move:
    print("Its a tie")
else:
    print("Invalid")