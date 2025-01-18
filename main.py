import random
def playagain():
    choice = ["no", "yes"]
    while True:
        try:
            replay = input("\nDo u wish to play again? ").lower()
            if replay not in choice:
                print(f"\nInvalid input \"{replay}\". Enter either (YES or NO)")
                continue
            elif replay == "yes":
                print()
                playGame()
            else:
                print("\nThanks for playing ;)!")
            break
        except ValueError:
            print(f"\nInvalid input \"{replay}\". Choose either YES or NO!")
        
                
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
        while True:
            try:
                user_choice = input("\nEnter rock, paper or scissors: ").lower()
                if user_choice not in choices:
                    print("\nInvalid input. Enter either rock, paper or scissors")
                    continue
                break
            except ValueError:
                print("Invalid input. Enter either rock, paper or scissors")
            

        computerChoice = random.choice(choices)
        print(f"Computer plays {computerChoice}")

        if user_choice == computerChoice:
            print("\nIts a tie")
            print(f"Score: Computer:{computerPoint} \nPlayer:{playerPoint}")

        elif (user_choice == "rock" and computerChoice == "scissors") or \
             (user_choice == "scissors" and computerChoice == "paper") or \
             (user_choice == "paper" and computerChoice == "rock"):
            playerPoint+=1
            print("\nYou win this round!")
            print(f"Score: Computer:{computerPoint} \nPlayer:{playerPoint}")
        else:
            print("\nyou lose this round!")
            computerPoint+=1
            print(f"Score: Computer:{computerPoint} \nPlayer:{playerPoint}")

        if playerPoint == maxPoint:
            print("\nCongrats you have won the game!")
            break
        elif computerPoint == maxPoint:
            print("\nYou have lost the game. Better luck next time")
            break
    if playerPoint != maxPoint and computerPoint != maxPoint:
        print("\nFinal Results:")
        print(f"\nYour points: {playerPoint} \nComputer's points: {computerPoint}")

        if playerPoint > computerPoint:
            print("You are the winner!")
        elif computerPoint > playerPoint:
            print("The computer is the winner!")
        else:
            print("It's a tie!")      
    playagain()
playGame()