import sys


def titleScreen():
        print("""

        \t\t\t HEIST OF THE CENTURY
        \t\t\t*$*$*$*$*$*$*$*$*$*$*$*
        \t\t\tText Based Adventure Game
        \t\t\t   by Tyrese Richards""")
        
        print(
        """
        \t\t\t[1]New Game
        \t\t\t[2]Continue
        \t\t\t[3]Highscores
        \t\t\t[4]How to play
        \t\t\t[5]Exit
        """)
        option = input("\t\t\t\tChoose an option: ")
        if option == "1":
            newGame()
        elif option == "2":
            continueGame()
        elif option == "3":
            highScores()
        elif option == "4":
            how_to_play()
        elif option == "5":
            sys.exit(exitGame())
        else:
            print("\nInvalid Option.")

def newGame():
    planStage()
    #startStage()
    #bankStage()
    #moneyStage()
    #exitStage()

def planStage():
    print("It's exactly a month before the heist and you need to prepare.")
    print("\nYou open up a document containing 2 potential partners.")
    print("\nThe first page contains a Lowlife gangster from the Brick Burners gang,",
          "\nBrick Burners are known for their ability to hotwire cars and a;ways carry an UZI.",
          "\nThe second page contains an Ex-CIA agent known for his effectiveness in assisting anti-socialism coups.")
    print("1. Lowlife Gangster",
          "2. Ex-CIA Agent")
    partner = input("Which partner do you choose: ")
    if partner == '1':
        startStage1()
    elif partner == '2':
        startStage2()
    else:
        print("\nInvalid Choice!")

def startStage1():
        global score
        print("\nYou pull into the alley way across from the bank.",
              "\nIt's time to start the heist",
              "\nYou and the BB gangster put on your mask and make your way to the bank entrance")
        print("\nYou shout 'EVERYBODY THIS IS A ROBBERY' and wave your gun at the crowd",
              "\nThe BB gangster nods implying to make a move")
        print("\nThe heist plan is a little foggy in your head because of situation",
              "\nA split decision is required before someone in the crowd decides to play hero")
        print("You can either: ",
              "\n1. Tell everyone to get on the ground and tie up the hostages or",
              "\nTell the gangster to take a hostage and hold up the lobby")
        actionOne = input("Make a decision: ")
        if actionOne == '1':
            score += 1
            bankStage()
        elif actionOne == '2':
            print("The gangster runs over to the crowd to grab a hostage,",
                  "\nNot realising his shoe laces are untied, he falls over and accidentally unloads uzi on the crowd",
                  "\nThe plan was not to kill any hostages knowing that you'll get a life sentence the heist is over",
                  "\nGAME OVER!")
            titleScreen()
        else:
            print("\nInvalid decision")

def startStage2():
    global score
    print("\nYou climb off the fire escape on to the GNB rooftop.")
    print("It's time to start the heist")
    print("As you locate the area above the vault, a guard appears by the rooftop entrance, 'he must be on his break' says the agent")
    print("Before he turns around and spots you, you and your partner must make a move",
          "\nYou can: ",
          "\n1. Shoot the guard and hide the body",
          "\n2. Distract the guard or",
          "\n3. Ignore the guard and hope he dies in the blast")
    optionOne = input("Make a move: ")
    if optionOne == '1':
        print("You take out the guard with the silenced pistol and hide the body on the back of the rooftop entrance")
        score += 1
    elif optionOne == '2':
        print("The agent moves to distract the guard but coughs and the guard hears him",
              "\nbefore the guard can react the agent pushes him off the room, he lands in",
              "\nthe skip below")
        score += 1
    elif optionOne == '3':
        print("Ignoring the guard you go to plan the C4 but the guard spots you and opens fire, realising that your plans have failed",
              "\nthe agent makes his way out of there",
              "\nGAME OVER!")
        titleScreen()
    else:
        print("\nInvalid option")
    print("\nYou plant the C4 and detonate it after taking a cover.",
          "\nThe roof opens up, the agent throws a ladder down",
          "and you both enter the bank but it;s not the vault it's the lobby!")
    bankStage()
    

def bankStage():
    global score
    print("\nYou tie everyone and take a hostage for insurance: The bank manager.",
          "\nAs you head down the hallway from the lobby, 2 rooms appear before you: The teller's desk or the main vault",
          "\nThe heist is underway and everything is going as planned")
    print("You can either:",
            "\n1. Take the bank manager into the teller's desk and get some quick cash though it's not what you came for. or",
            "\n2. Take the bank manager to the bank vault")
    actiontwo = input("Make a decision: ")
    if actiontwo == '1':
        print("While dragging the uncooperative bank manager to the desk, you let go and aim your gun whilst telling him to open the drawers",
              "\nunable to see the right side of him, the manager manages to press the silent alarm, alerting the police and failing your plans to rob the bank",
              "\nGAME OVER!")
        titleScreen()
    elif actiontwo == '2':
        print("You take the 2nd door to the main vault, forcing the manager to enter the vault code, you knock out the bank manager as it's time to make some money")
        score += 1
        vaultStage()
    else:
        print("\nInvalid decision")

def vaultStage():
    global score
    print("\nAs you and the your partner enter the vault, surrounded by money piles and lockboxes, your partner suggests that you should get a little bit of extra money",
          "\nto ensure that the total is higher in case money gets lost in the getaway")    
    print("Knowing that an aversion to the plan could mean an unsuccessful heist you must make another descion")
    print("You can either:",
          "\n1. Open up some lock-boxes for extra cash or",
          "\n2. Start bagging up the money piles")
    actionthree = input("Make a decision: ")
    if actionthree == '1':
        print("That's an extra 250k bonus")
        score += 3
        actionfour = input("Do you want to open up more lock-boxes? (y/n): ")
        if actionfour == 'y':
            print("Unfourtunately just like greed being 1 of 7 carnal sins, whilst unlocking them you don't notice the security guard and end up dead in 7 seconds!")
            print("GAME OVER!")
            titleScreen()
        elif actionfour == 'n':
           moneyStage1()
    elif actionthree == '2':
        moneyStage1()

def moneyStage1():
    global score
    money = 0
    actionfive = input("\nTake 10 million? (y/n): ")
    money += 10
    while(actionfive == 'y'):
        actionsix = input("Take another 10 million? (y/n): ")
        if actionsix == 'y':
                money += 10
                score += 1
                if money == 50:
                        exitStage1()
                elif money >50:
                        print("The money weighs too much you break your spinal cord and die")
                        titleScreen()
        elif actionsix == 'n':
                print("It's time to get out of here!")
                exitStage1()
                
    if actionfive == 'n':
        print("What was the point in doing the heist then!")
        print("\nGAME OVER!")
        titleScreen()

def moneyStage2():
    global score
    money = 0
    actionfive = input("\nTake 10 million? (y/n): ")
    money += 10
    while(actionfive == 'y'):
        actionsix = input("Take another 10 million? (y/n): ")
        if actionsix == 'y':
                money += 10
                score += 1
                if money == 50:
                        exitStage2()
                elif money >50:
                        print("The money weighs too much you break your spinal cord and die")
                        titleScreen()
        elif six == 'n':
                print("It's time to get out of here!")
                exitStage2()
                
def exitStage1():
    global score
    print("Bursting out of the front door of the bank, you hear growing roar of police sirens headed towards the bank",
          "\n'I can hotwire this car dude, then we can get the hell out of here' says the gangster,",
          "\nThe plan says go back to the car we came in but the police are almost here")
    print("You can either: ",
          "\n1. Hotwire the car in front of the bank or",
          "\n2. Run across the street and go to the orignal car")
    actionseven = input("Make a decision: ")
    if actionseven == '1':
        print("The car is hotwired without an issue, you take off into the sunset passing the police without getting any heat",
              "\nCongrats You Won!")
        score += 1
        print("Your Score is: ",score)
        titleScreen()

    elif actionseven == '2':
        print("Before you could make it to the alley a police sniper takes you and your partner out")
        print("GAME OVER!")
        titleScreen()
         
def exitStage2():
    global score
    print("\n'Let's get to the roof' says the agent, but the plan says leave him in the vault so he can't tell the police which way we went",
          "\nhowever by taking the bank manager to the roof means that you can either use him as a body shield so the police aren't able",
          "\nto take a shot at you and the agent or use him in negotiations for a chopper meaning a quicker escape")
    print("\nYou can either: ",
          "\n1. Use him as a body shield or",
          "\n2. Use him as a bargining chip for a chopper")
    actioneight = input("Make a move: ")
    if actioneight == '1':
            print("You and the agent move the bank manager down the fire escape, crossing the street to the starting car you use him as the",
                  "\nbank manager as a body shield so the police can't get a clear shot")
            print("\nYou and the agent make it into the car and escape with a small heat on your trail!",
                  "\nCongrats You Won!")
            score += 1
            print("Your Score is: ",score)
            titleScreen()
    elif actioneight == '2':
            print("You shout to the police that for a chopper you'll release the hostages and the bank manager for a helicopeter to the airport",
                  "\nThe police being the police agree but almost immediately tells the sniper to take you out once the hostages are safe,"
                  "\nGAME OVER!")
            titleScreen()
            


    
        
def continueGame():
    while(True):
            print("""
            1. Start Stage
            2. Bank Stage
            3. Vault Stage
            4. Money Stage
            5. Exit Stage
            """)
            actionnine = input("What Stage did you end on?: ")
            if actionnine == '1':
                    actionten = input("Start Stage 1 (Lowlife Gangster) or Start Stage 2 (Ex-CIA Agent)")
                    if actionten == 'Start Stage 1':
                            startStage1()
                            break
                    elif actionten == 'Start Stage 2':
                            startStage2()
                            break
                    else:
                            print("Enter either Start Stage 1 or Start Stage 2")
            elif actionnine == '2':
                    bankStage()
                    break
            elif actionnine == '3':
                    vaultStage()
                    break
            elif actionnine == '4':
                    actionten = input("Money Stage 1 (Lowlife Gangster) or Money Stage 2 (Ex-CIA Agent)")
                    if actioneleven == 'Money Stage 1':
                            moneyStage1()
                            break
                    elif actioneleven == 'Money Stage 2':
                            moneyStage2()
                            break
                    else:
                            print("Enter either Money Stage 1 or Money Stage 2")
            elif actionnine == '5':
                    actiontwelve = input("Exit Stage 1 (Lowlife Gangster) or Exit Stage 2 (Ex-CIA Agent)")
                    if actiontwelve == 'Exit Stage 1':
                            exitStage1()
                            break
                    elif actiontwelve == 'Exit Stage 2':
                            exitStage2()
                            break
                    else:
                            print("Enter either Exit Stage 1 or Exit Stage 2")
            else:
                    print("Invalid Option")
            
def highScores():
        global score
        highScore = get_high_score()
        currentScore = 0
        currentScore += score
        try:
                currentScore = int(input("What's your score: "))
        except VauleError:
                print("Invalid Input")

        if currentScore > highScore:
                print("New High Score")
                highScore_save(currentScore)
        elif currentScore < highScore:
                print("New Score Added")
                highScore_new(currentScore)
        else:
                print("No Score Inputted")
        return highScore
        
def get_high_score():
    highScore = 0

    try:
            highScore_file = open("HighScores.txt", "r")
            highScore = int(highScore_file.read())
            highScore_file.close()
            print("The Current High Score: ", highScore)
    except IOError:
            print("No High Score")
    except ValueError:
            print("Unreadable Data")

    return highScore

def highScore_save(highScore_save):
    try:
          highScore_file = open("HighScores.txt", "r")
          highScore_file.write(str(highScore_save))
          highScore_file.close()
    except IOError:
             print("Unable to save Highscore")

def highScore_new(highScore_new):
    try:
          highScore_file = open("HighScores.txt", "a")
          highScore_file.write("\n")
          highScore_file.write(str(highScore_new))
          highScore_file.close()
    except IOError:
             print("Unable to save Highscore")

def how_to_play():
    print("""
    HOW TO PLAY
    The game works by the player going through several stages,
    trying to go as far as you can, reach the end goal without failing.


    STORY
    Your a professional bank robber, about to rob the Grand National Bank for £100 million.
    You must pick a partner, choose the right equipment, make the right choices in high action situations,
    to pull of the heist of the century!
    """)
    
def exitGame():
    print()
    print("You successfully pulled of the heist of the century",
          "\nThanks for playing!")

#main
score = 0
while(True):
    titleScreen()
    
    

        
