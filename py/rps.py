import random

choices = [ "rock", "paper", "scissors" ]
pInput = input("Select Rock, Paper, or Scissors to play!\nPlayer: ")


while pInput.lower() not in choices:
    pInput = input("Please try again\ntype \"rock\", \"paper\", or \"scissors\" to play.\nPlayer: ")

pInput = pInput.capitalize()# pInput.lower()[:1].upper() + pInput[1:]
cInput = random.choice(choices).capitalize()
print(f"Computer: {cInput}")



def checkMoves(pi, ci):
    currentMatch = f"{pi} vs. {ci}"
    if pi == ci:
        print(f"{currentMatch} is a draw!")
    
    if pi == "Rock":
        if ci == "Scissors":
            print(f"{currentMatch}, You win!")
        if ci == "Paper":
            print(f"{currentMatch}, Computer wins!")

    if pi == "Paper":
        if ci == "Rock":
            print(f"{currentMatch}, You win!")
        if ci == "Scissors":
            print(f"{currentMatch}, Computer wins!")

    if pi == "Scissors":
        if ci == "Paper":
            print(f"{currentMatch}, You win!")
        if ci == "Rock":
            print(f"{currentMatch}, Computer wins!")

checkMoves(pInput, cInput)

# to do: make scores, 5 points to win
# unfinished if you couldn't tell