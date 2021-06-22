import computer as c
import functions as f
#start of round...
quitGame = True
keepPlaying = True
print("_____________________________________________")
print("| Let's start the Rock, Paper, Scissors game |")
print("_____________________________________________")
print("You will be the first to start the game!!")

while quitGame == True:
    userInput = input("Choose between: \nRock \nPaper \nScissors \nQuit (if you'd like to exit) \n")
    if userInput.lower() == "quit":
        quitGame = False
        break
    elif userInput.lower() == "rock" or userInput.lower() == "scissors" or userInput.lower() == "paper":
        f.addInput(userInput)
        print(c.waitForCom)
        print("..............")
        print("Computer's choice: ",c.choice)
        f.updateUserScore(userInput,c.choice)
    else:
        print("INVALID")

#At the end of the game print the scores
print("Your Score:")
print(f.printUserScore())
print("Computers Score:")
print (f.printComputerScore())