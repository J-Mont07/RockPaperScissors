import score as score

#Checks for valid user input
def checkInput(user):
    f = True
    while f == True:
        if ((user.lower() == "rock") or (user.lower() == "paper") or (user.lower() == "scissors") or (user.lower() == "quit")):
            f = False
            break
        else:
            print("INVALID INPUT")
            user = input("Choose between: \nRock \nPaper \nScissors \nQuit \n")
            f = True

#Updates the times user choose either Rock Paper Scissor
def addInput(user):
    r = 0
    s = 0
    p = 0
    if (user.lower() == "scissors"):
        s = s + 1
        score.userChoice["scissors"] = s
    if(user.lower() == "rock"):
        r = r + 1
        score.userChoice["rock"] = r
    if (user.lower() == "paper"):
        p = p + 1
        score.userChoice["paper"] = p
def updateUserScore(user,com):
    cw = 0
    cl = 0
    t = 0

    w = 0
    l = 0
    if user == com:
        print("TIE")
        t = t + 1
        score.userScore["Tie"] = t
        score.computerScore["Tie"] = t
    else:
        if (user == "rock") & (com == "scissors"):
            print("YOU WIN!!")
            w = w + 1
            cl = cl + 1
            score.userScore["Wins"] = w
            score.computerScore["Loss"] = cl

        elif (com == "rock") & (user == "scissors"):
            print("Computer Wins!!")
            cw = cw + 1
            l = l + 1
            score.computerScore["Wins"] = cw
            score.userScore["Loss"] = l

        if (user == "rock") & (com == "paper"):
            print("Computer Wins!!")
            cw = cw + 1
            l = l + 1
            score.computerScore["Wins"] = cw
            score.userScore["Loss"] = l

        elif (user == "paper") & (com == "rock"):
            print("YOU WIN!!")
            w = w + 1
            cl = cl + 1
            score.userScore["Wins"] = w
            score.computerScore["Loss"] = cl

        if (user == "scissors") & (com == "paper"):
            print("YOU WIN!!")
            w = w + 1
            cl = cl + 1
            score.userScore["Wins"] = w
            score.computerScore["Loss"] = cl

        elif (com == "scissors") & (user == "paper"):
            print("Computer Wins!!")
            cw = cw + 1
            l = l + 1
            score.computerScore["Wins"] = cw
            score.userScore["Loss"] = l



#Prints the time user choose Rock Paper Scissor
def printUserChoice():
    for x,y in score.userChoice.items():
        print(x,y)

#Prints the users Win loss and ties
def printUserScore():
    for x,y in score.userScore.items():
        print(x,y)
#prints computers wins loss and ties
def printComputerScore():
    for x,y in score.computerScore.items():
        print(x,y)