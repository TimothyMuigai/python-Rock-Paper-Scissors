import random
def playagain():
    choice = ["no", "yes"]
    while True:
        try:
            replay = input("Do u wish to play again? ")
            if replay not in choice:
                print("Invalid input. Choose either YES or NO!")
                continue
            break
        except ValueError:
            print("Invalid input. Choose either YES or NO!")
        finally:
            if replay == "yes":
                playGame()
            else:
                print("thansk for playing ;)!")
                
def playGame():
    while True:
        try:
            roundChoice = int(input("Enter between 3 or 5 rounds: "))
            if roundChoice not in [3,5]:
                print("Invalid number. Please Enter a number either 3 or 5")
                continue
            break
        except ValueError:
            print("invalid input. Please Enter a number either 3 or 5")
    
    
    choices = ["rock","paper","scissors"]    
    maxPoint = roundChoice // 2+1

    playerPoint = 0
    computerPoint = 0
    roundCount = 0 

    while roundCount < roundChoice:
        print(f"\nRound {roundCount+1} out of {roundChoice}")
        roundCount+=1
        user_choice = input("Enter rock, paper or scissors: ").lower()
        if user_choice not in choices:
            print("Invalid input. Enter either rock, paper or scissors")
            continue

        computerChoice = "rock"
        print(f"Computer plays {computerChoice}")

        if user_choice == computerChoice:
            print("its tie")
        elif (user_choice == "rock" and computerChoice == "scissors") or \
             (user_choice == "scissors" and computerChoice == "paper") or \
             (user_choice == "paper" and computerChoice == "rock"):
            playerPoint+=1
            print("You win this round!")
        else:
            print("you lose this round!")
            computerPoint+=1

        if playerPoint == maxPoint:
            print("\nCongrats you have won the game!")
            break
        elif computerPoint == maxPoint:
            print("\nYou have lost the game. Better luck next time")
            break
    if playerPoint != maxPoint and computerPoint != maxPoint:
        print("\nFinal Results:")
        print(f"Your points: {playerPoint}")
        print(f"Computer's points: {computerPoint}")

        if playerPoint > computerPoint:
            print("You are the winner!")
        elif computerPoint > playerPoint:
            print("The computer is the winner!")
        else:
            print("It's a tie!")      
    playagain()
playGame()