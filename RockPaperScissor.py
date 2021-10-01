
# //Rock Paper Scissor
# Rock vs paper = Rock
# Paper vs Rock  = paper
# Scissor vs paper = scissor
# Rock vs Scissor = Rock
import random
n = random.randint(0,2)
print(f"Generated Random Number is: {n}")
computer = ["rock", "paper", "scissor"]
print(f"Computer selects : {computer[n]}")
print("_________________________________")
print()

while True:
    player = input("Enter Rock or Paper or Scissor: ").lower()
    if player == "rock" or player == "paper" or player == "scissor":
        for i in range(3):
    # if computer[n] == "rock":
            if computer[n] == "rock" and player == "rock":
                # It's a Tie
                print(f"{computer[n]} vs {player} It is Tie")

            elif computer[n] == "rock" and player == "scissor":
                # Rock smashes Scissors - computer wins
                print(f"{computer[n]} smashes scissors and computer wins")

            elif computer[n] == "rock" and player == "paper":
                # Paper covers the Roack  - player wins
                print(f"{player} covers {computer[n]} player wins")


    # elif computer[n] == "scissor":
            if computer[n] == "scissor" and player == "scissor":
                # It's a Tie
                print(f"{computer[n]} vs {player} It is Tie")

            elif computer[n] == "scissor" and player == "paper":
                # Scissor cut Paper computer wins
                print(f"{computer[n]} cuts {player} and computer wins")

            elif computer[n] == "scissor" and player == "rock":
                # Rock smashes scissor
                print(f"{player} smashes {computer[n]} and computer wins")

    # elif computer[n] == "paper":
            if computer[n] == "paper" and player == "paper":
                # It's a Tie
                print(f"{computer[n]} vs {player} It is Tie")

            elif computer[n] == "paper" and player == "scissor":
                # Scissor cut Paper
                print(f"{player} cuts {computer[n]} and player wins")

            elif computer[n] == "paper" and player == "rock":
                # Paper covers Rock
                print(f"{computer[n]} covers {player} and computer wins")

print("Print Loop Ended")








