# Creating a rock paper scissors game! 
# It will be the user vs the computer. It will be a best of 5!

import random 

choices = ["rock", "paper", "scissors"]
computer_wins = 0
user_wins = 0

for value in range(5):
  computer = random.choice(choices) # telling the computer to choose either rock paper or scissors
  user = input("Enter your choice (rock, paper, or scissors): ") # user's turn
  print("Computer chose: " + computer)

  # if the user's choice and the computer's choice is the same -> tie
  if user == computer:
    print("Tie")
  elif (user == "rock" and computer == "scissors") or \
       (user == "paper" and computer == "rock") or \
       (user == "scissors" and computer == "paper"):
      # execute this
      print("You win this round!")
      user_wins += 1 # user_wins = user_wins + 1
  else:
    # computer wins
    print("Computer wins this round!")
    computer_wins += 1 # computer_Wins = computer_wins + 1

# execute 5 times 

# Printing the final score!
print("Final Score: ")
print("User score: " + str(user_wins)) # user score
print("Computer score: " + str(computer_wins)) # computer score 




