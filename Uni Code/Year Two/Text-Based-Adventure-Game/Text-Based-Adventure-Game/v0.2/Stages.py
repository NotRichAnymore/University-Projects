import sys
import Characters
import Events
import Menu
import Stages
import random
import pygame
import shelve

def newGame():
    planStage()
    #startStage()
    #bankStage()
    #moneyStage()
    #exitStage()

def planStage():
    #Displays story text
    print("It's exactly a month before the heist and you need to prepare.")
    print("You call up Dave to get sorted")
    Shop()
    print("Hopefully you got prepared, it'd be impossible without a loadout")
    print("\nYou open up a document containing 2 potential partners.")
    #Gives user options to pick their partner
    print("\nThe first page contains a Lowlife gangster from the Brick Burners gang,",
          "\nBrick Burners are known for their ability to hotwire cars.",
          "\nThe second page contains an Ex-CIA agent known for his effectiveness in assisting anti-socialism coups.")
    print("1. Lowlife Gangster",
          "2. Ex-CIA Agent")
    #Chooses which storyline to go through depending on the partner
    partner = input("Which partner do you choose: ")
    if partner == '1':
        startStage1()
    elif partner == '2':
        startStage2()
    else:
        #If Player doesn't input a given choice asked again
        print("\nInvalid Choice!")
    
#First stage for first storyline
def startStage1():
        #Global variables allows each function to access them not overwrite
        global game_score
        global hostage_death
        #Displays story
        print("\nYou pull into the alley way across from the bank.",
              "\nIt's time to start the heist",
              "\nYou and the BB gangster put on your mask and make your way to the bank entrance")
        print("\nYou shout 'EVERYBODY THIS IS A ROBBERY' and wave your gun at the crowd",
              "\nThe BB gangster nods implying to make a move")
        print("\nThe heist plan is a little foggy in your head because of situation",
              "\nA split decision is required before someone in the crowd decides to play hero")
        print("You can either: ",
              "\n1. Tell everyone to get on the ground and tie up the hostages or",
              "\n2. Tell the gangster to take a hostage and hold up the lobby")
        #User input to move to next stage
        actionOne = input("Make a decision: ")
        if actionOne == '1':
            #Adds to player's score
            game_score += 1
                
            print('Score: ', game_score)
            bankStage()
        elif actionOne == '2':
            print("The gangster runs over to the crowd to grab a hostage,",
                  "\nNot realising his shoe laces are untied, he falls over and accidentally unloads uzi on the crowd",
                  "\nThe gun shots might have alerted the police in the area")
            #Adds to score negatation
            hostage_death += 1
            #Instead of fail state, potential to fail through raid function
            raid()
            print('Score: ', game_score)
            #Move to next stage if haven't failed in raid function
            bankStage()
        else:
            print("\nInvalid decision")
        

def startStage2():
    global game_score
    global IsC4Equipped
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
        game_score += 1
    elif optionOne == '2':
        print("The agent moves to distract the guard but coughs and the guard hears him",
              "\nbefore the guard can react the agent pushes him off the room, he lands in",
              "\nthe skip below")
        game_score += 1
    elif optionOne == '3':
        print("Ignoring the guard you go to plant the C4, he breaks out of sight",
              "\nhe might have called for backup or have not noticed")
        raid()
    else:
        print("\nInvalid option")

    #Displays C4 Storyline part only if it has been purchased
    if IsC4Equipped == True:
        print("\nYou plant the C4 and detonate it after taking a cover.",
              "\nThe roof opens up, the agent throws a ladder down",
              "and you both enter the bank but it's not the vault it's the lobby!")
        game_score += 1
        print('Score: ', game_score)
        bankStage()
    elif ISC4Equipped == False:
        print("\nThe coast is clear and you sneak down the stairs from the rooftop",
              "\nas the pair of you enter the main corridor sneaking towards the lobby",
              "\nyou have to walk past a crowd of people drawing attention")
        raid()
        game_score -= 1
        print('Score: ', game_score)
        bankStage()    

def bankStage():
    global game_score
    print("\nYou tie everyone and take a hostage for insurance: The bank manager.",
          "\nAs you head down the hallway from the lobby, 2 rooms appear before you: The teller's desk or the main vault",
          "\nThe heist is underway and everything is going as planned")
    print("You can either:",
            "\n1. Take the bank manager into the teller's desk and get some quick cash though it's not what you came for. or",
            "\n2. Take the bank manager to the bank vault")
    actiontwo = input("Make a decision: ")
    if actiontwo == '1':
        print("While dragging the uncooperative bank manager to the desk, you let go and aim your gun whilst telling him to open the drawers",
              "\nunable to see the right side of him, the manager manages to press the silent alarm, possibly alerting the police")
        raid()
        game_score -= 1    
        print('Score: ', game_score)
        vaultStage()
    elif actiontwo == '2':
        print("You take the 2nd door to the main vault, forcing the manager to enter the vault code, you knock out the bank manager as it's time to make some money")
        game_score += 1    
        print('Score: ', game_score)
        vaultStage()
    else:
        print("\nInvalid decision")

def vaultStage():
    global game_score
    global player
    global IsDrillEquipped
    player = player
    print("\nAs you and the your partner enter the vault, surrounded by money piles and lockboxes, your partner suggests that you should get a little bit of extra money",
          "\nto ensure that the total is higher in case money gets lost in the getaway")    
    print("Knowing that an aversion to the plan could mean an unsuccessful heist you must make another descion")
    print("You can either:",
          "\n1. Open up some lock-boxes for extra cash or",
          "\n2. Start bagging up the money piles")
    actionthree = input("Make a decision: ")
    if actionthree == '1':
        if IsDrillEquipped == True:
            print("That's an extra 250k bonus")
            #Adds money which effects the overall score
            player.money += 250000
            game_score += 3
            actionfour = input("Do you want to open up more lock-boxes? (y/n): ")
            if actionfour == 'y':
                print("Unfourtunately just like greed being 1 of 7 carnal sins, whilst unlocking them you don't notice the security guard!")
                raid()
                game_score -= 1
                print('Score: ', game_score)
                moneyStage1()
            elif actionfour == 'n':
               print('Score: ', game_score)
               moneyStage1()
        #If the user hasn't purchased the drill can't open lockboxs
        elif IsDrillsEquipped == False:
            print("You didn't buy a drill, so you start bagging up money")
            print('Score: ', game_score)
            moneyStage1()
    elif actionthree == '2':
        print('Score: ', game_score)
        moneyStage1()

def moneyStage1():
    global game_score
    global player
    player = player
    money = 0
    actionfive = input("\nTake 10 million? (y/n): ")
    #Asks user to take 10 million each time until they try to take more than 50 million in which they fail
    while(actionfive == 'y'):
        actionsix = input("Take another 10 million? (y/n): ")
        player.money += 1000000
        money += 10
        if actionsix == 'y':
                money += 10
                game_score += 1
                if money == 50:
                        print('Score: ', game_score)
                        exitStage1()
                elif money >50:
                        print("The money weighs too much you break your spinal cord and die")
                        print('Score: ', game_score)
                        titleScreen()
                        break
        elif actionsix == 'n':
                print("It's time to get out of here!")
                print('Score: ', game_score)
                exitStage1()
                break
                
    if actionfive == 'n':
        print("What was the point in doing the heist then!")
        print("\nGAME OVER!")
        print('Score: ', game_score)
        titleScreen()

def moneyStage2():
    global game_score
    global player
    player = player
    money = 0
    actionfive = input("\nTake 10 million? (y/n): ")
    #Asks user to take 10 million each time until they try to take more than 50 million in which they fail
    while(actionfive == 'y'):
        actionsix = input("Take another 10 million? (y/n): ")
        player.money += 1000000
        money += 10
        if actionsix == 'y':
                money += 10
                game_score += 1
                if money == 50:
                        print('Score: ', game_score)
                        exitStage2()
                elif money >50:
                        print("The money weighs too much you break your spinal cord and die")
                        print('Score: ', game_score)
                        titleScreen()
                        break
        elif actionsix == 'n':
                print("It's time to get out of here!")
                print('Score: ', game_score)
                exitStage2()
                break
                
    if actionfive == 'n':
        print("What was the point in doing the heist then!")
        print("\nGAME OVER!")
        print('Score: ', game_score)
        titleScreen()
                
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
        game_score += 1
        #Displays final score accumlated through the game
        print("Your Score is: ",game_score)
        titleScreen()

    elif actionseven == '2':
        print("Before you could make it to the alley a police sniper takes you a shot")
        raid()
        game_score -= 1
        exitStage1()
                 
def exitStage2():
    global game_score
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
            game_score += 1
            print("Your Score is: ",game_score)
            titleScreen()
    elif actioneight == '2':
            print("You shout to the police that for a chopper you'll release the hostages and the bank manager for a helicopeter to the airport",
                  "\nThe police being the police agree but almost immediately tells the sniper to take you out once the hostages are safe,")
            raid()
            print('Score: ', game_score)
            game_score -= 1
            exitStage2()
