import sys
import random
import pygame
import shelve

#Classes for the player, enemies and pickups
class Item:
    def _init_(self):
        self.name = name
        self.description = description
        self.value = value
        self.damage = damage
        self.health = health
        self.money = money

class player:
    def _init_(self):
        self.damage = damage
        self.health = health
    health = 100
    damage = 0
    money = 10000
    weapon = 'unarmed'
    armour = 'suit'   

class hostage:
    def _init_(self):
        self.health = 1
        self.damage = 0
    
class policeOfficer:
    def _init_(self):
        self.health = health
        self.damage = damage
    damage = 20
    health = 50
    name = 'Police Officer'

class riotPolice:
    def _init_(self):
        self.health = health
        self.damage = damage
    damage = 35
    health = 65
    name = 'Riot Police'

def titleScreen():
    #Displays title screen
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
        #User input move to the next option
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

def raid():
    #Intialise variables
        global game_score
        global player
        player = player
        battle = False
        locked = False
        enemy_class = policeOfficer
        enemy = enemy_class
        enemy_name = enemy_class.name
        #Starts the raid
        ans = input('You come to a room, continue (Y/N)')
        if ans == 'y':
                raid = random.randint(1,100)
                if raid < 40:
                        locked = True
                        #
                        while locked == True:
                                rob = input('A hostage hides a bag as if it has some value, do you want to take their bag (Y/N)')
                                if rob == 'y':
                                        print('You point the gun at the hostage and they empty their wallet')
                                        player.money += 200
                                        player.health += 20
                                        print(' You recived £200 and some painkillers (+20 health')
                                        break

                                elif rob == 'n':
                                        continue
                elif raid >= 40:
                        battle = True
                        #Creates battle scenario
                        while battle == True:
                                if player.weapon == 1:
                                        enemy_class = random.choice([policeOfficer, riotPolice])
                                elif player.weapon == 2:
                                        enemy_class = policeOfficer
                                #Assigns enemy classes to usable variables
                                
                        
                                print('Someone managed to press the silent alarm...')
                                print(f'{enemy_name} enter the bank during a raid')
                                #Check to perform raid only if player or enemey hasn't died
                                while enemy.health > 0 or player.health > 0:
                                        user = input('Press s to shoot: ')
                                        if user == 's':
                                                enemy.health = enemy.health - player.damage
                                                print(f'The {enemy_name} took {player.damage} damage')
                                        #End raid if enemey died
                                        if enemy.health <= 0:
                                                print('The police raid is over')
                                                game_score += 1
                                                battle = False
                                                break
                                        #Gives enemy damage debuff
                                        if user == 's':
                                                player.health = player.health - enemy.damage
                                                enemy.damage = enemy.damage + random.choice([-5, 0])
                                                if enemy.damage > 0:
                                                    print(f'The {enemy.name} manged to hit you and dealt {enemy.damage} damage')
                                        #Ends raid if player died
                                        if player.health <= 0:
                                                print('You got shot too much you pass out from the pain')
                                                player.health = 50
                                                print('Your partner managed to finish them off, you continue the heist')
                                                battle = False
                                                break
        #Avoids raids and chance to gain bonuses
        elif ans == 'n':
                print('You wait for you partner to make a move then folow them to the next room')
                
def Shop():
        #Intialises player class for shop function
        global player
        player = player
        checkout = {}
        #Dictionary to contain items available to purchase
        stock = {'Uzi':'Automatic Submachine Gun, £4k','Silenced Pistol':'Semi Auto Stealth Pistol, £6.5k',
                 'Light Armour':'Made of Polycarbon Fibre, £1k','Heavy Armour':'Kevlar Armour, £2.5k',
                 'C4':'Plastic Explosive, £2k','Industrial Drill':'Battery Powered, can break through steel, £1.5k'}
        #Assigns price variables for shop iems        
        uzi_price = 4000
        sp_price = 6500
        al_price = 1000
        ah_price = 2500
        c4_price = 2000
        id_price = 1500
        #Instislise variables to check if the player has that item equipped
        global IsUziEquipped
        global IsPistolEquipped
        global IsArmourLEquipped
        global IsArmourHEquipped
        global IsC4Equipped
        global IsDrillEquipped
        #Beginning of Shop function
        shop = input("Dave's Dodgy Deals, Do you want something (Y/N)")
        if shop == 'y':
            #Loops shop function 
                while(True):
                    print('Dave shares a screen full of ill gotten goods')
                    ans = input('Do you want to see some weapons (Y/N)')
                    #Displays Current player money
                    print('Heist funds: ',player.money)
                    if ans == 'y':
                        #Allows the user to buy a weapon only if they havent already
                        if IsUziEquipped == False and IsPistolEquipped == False:
                            while(True):
                                #Displays items
                                print('Uzi: ',stock['Uzi'])
                                print('Silenced Pistol: ',stock['Silenced Pistol'])
                                option = input('Which of these weapons do you want?: ')
                                if option == 'Uzi':
                                               #Checks if player has the money to purchase the item 
                                               if player.money < uzi_price:
                                                       print('You dont have the funds')
                                               #Adds effects to player class 
                                               elif player.money >= uzi_price:
                                                       player.money -= uzi_price
                                                       player.damage += 30
                                                       #Adds purchased items to a list (reciept)
                                                       checkout['Uzi'] = 'Automatic Submachine Gun'
                                                       #Player given weapon equipped status to prevent having mutliple damage bonuses
                                                       IsUziEquipped = True
                                                       break
                                elif option == 'Silenced Pistol':
                                        if player.money < sp_price:
                                                print('You dont have the funds')
                                        elif player.money >= sp_price:
                                                player.money -= sp_price
                                                player.damage += 20
                                                checkout['Silenced Pistol'] = 'Semi Auto Stealth Pistol'
                                                IsPistolEquipped = True
                                                break
                                #Repeats loop if player enters wrong option
                                else:
                                        print('Hurry up and choose a weapon')
                        #Goes to next items if this item is already equipped
                        else:
                            print('You already have a weapon')
                                    
                    ans2 = input('\nDo you want to see some armour (Y/N)')
                    print('Heist funds: ',player.money)
                    if ans2 == 'y':
                        if IsArmourLEquipped == False or IsArmourHEquipped == False:
                            while(True):
                                print('Light Armour: ',stock['Light Armour'])
                                print('Heavy Armour: ',stock['Heavy Armour'])
                                option = input('Which of these Equipment do you want?: ')
                                if option == 'Light Armour':
                                               if player.money < al_price:
                                                       print('You dont have the funds')
                                               elif player.money >= al_price:
                                                       player.money -= al_price
                                                       player.health += 10
                                                       checkout['Light Armour'] = 'Made of Polycarbon Fibre'
                                                       IsArmourLEquipped = True
                                                       break
                                elif option == 'Heavy Armour':
                                        if player.money < ah_price:
                                                print('You dont have the funds')
                                        elif player.money >= ah_price:
                                                player.money -= ah_price
                                                player.health += 25
                                                checkout['Heavy Armour'] = 'Kevlar Armour'
                                                IsArmourHEquipped = True
                                                break
                                else:
                                        print('Hurry up and choose some armour')
                        else:
                            print('You already have some armour')
                                    
                    ans3 = input('\nDo you want to see some equipment (Y/N)')
                    print('Heist funds: ',player.money)
                    if ans3 == 'y':
                        if IsC4Equipped == False or IsDrillEquipped == False:
                            while(True):
                                print('C4: ',stock['C4'])
                                print('Industrial Drill: ',stock['Industrial Drill'])
                                option = input('Which of these Equipment do you want?: ')
                                if option == 'C4':
                                               if player.money < c4_price:
                                                       print('You dont have the funds')
                                               elif player.money >= c4_price:
                                                       player.money -= c4_price
                                                       checkout['C4'] = 'Plastic Exsplosive'
                                                       IsC4Equipped = True
                                                       break
                                elif option == 'Industrial Drill':
                                        if player.money < id_price:
                                                print('You dont have the funds')
                                        elif player.money >= id_price:
                                                player.money -= id_price
                                                checkout['Industrial Drill'] = 'Battery Powered, can break through steel'
                                                IsDrillEquipped = True
                                                break
                                else:
                                        print('Hurry up and choose some equipment')
                        else:
                            print('You already have some armour')
                    #Ends Loop if player has finished purchasing items                    
                    ans4 = input('Are you finished? (Y/N): ')
                    if ans4 == 'y':
                        #Displays purchased items from a list
                         print("You've purchased these items:,",checkout ,"\nLooks like you'll be well prepared.")
                         break
                    elif ans4 == 'n':
                        #Restarts loop if player hasn't purchased anything
                        if IsUziEquipped == False or IsPistolEquipped == False or IsArmourLEquipped == False or IsArmourHEquipped == False or IsC4Equipped == False or IsDrillEquipped == False:
                            Shop()
                        #End loop if player has purchased 4 items
                        elif len(checkout) == 4:
                            break
                      
                            
                    
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
    print("You enter the vault and see stacks of money piled around the room, there must be hundreds of millions")
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
    print("You enter the vault and see stacks of money piled around the room, there must be hundreds of millions")
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
    global game_score
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
        
def continueGame():
    global player
    player = player
    Shop()
    while(True):
        #Displays continue menu
            print("""
            1. Start Stage
            2. Bank Stage
            3. Vault Stage
            4. Money Stage
            5. Exit Stage
            """)
            #Goes to stage depending on user input
            actionnine = input("What Stage did you end on?: ")
            if actionnine == '1':
                while(True):
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
                while(True):
                    actionten = input("Money Stage 1 (Lowlife Gangster) or Money Stage 2 (Ex-CIA Agent)")
                    if actionten == 'Money Stage 1':
                            moneyStage1()
                            break
                    elif actionten == 'Money Stage 2':
                            moneyStage2()
                            break
                    else:
                            print("Enter either Money Stage 1 or Money Stage 2")
                    
            elif actionnine == '5':
                while(True):
                    actiontwelve = input("Exit Stage 1 (Lowlife Gangster) or Exit Stage 2 (Ex-CIA Agent)")
                    if actioneleven == 'Exit Stage 1':
                            exitStage1()
                            break
                    elif actioneleven == 'Exit Stage 2':
                            exitStage2()
                            break
                    else:
                            print("Enter either Exit Stage 1 or Exit Stage 2")
            else:
                    print("Invalid Option")
            
def highScores():
        global score
        global hostage_death
        if hostage_death >= 1:
                score -= 4
        scoreFile = shelve.open('score.txt')

        def updateScore(newScore):
          if('score' in scoreFile):
            score = scoreFile['score']
            if(newScore not in score):
              score.insert(0, newScore)

            elif(newScore == score):
                print('You are tied at number', ranking)

            score.sort()
            ranking = score.index(newScore)
            ranking = len(score)-ranking
          else:
            score = [newScore]
            ranking = 1

          print('You are number',ranking,'on the leaderboard')
          print('Current scores: ',score)
          scoreFile['score'] = score
          return ranking

        print('SCORES')
        print('------')
        newScore = int(input("New HighScore: "))
        updateScore(newScore)

def how_to_play():
    #Displays how to play the game, the story, the objective etc.
    print("""
    HOW TO PLAY
    The game works by the player going through several stages,
    trying to go as far as you can, reach the end goal without failing.

    Before starting the game,
    their is an oppurunity to purchase a loadout for the raid,
    some items will benefit you more than others.

    Raids will take place throughout the game,
    in which you will have to fight off police raids.

    Be careful making the wrong choice(s) can lead to the death of hostages.

    STORY
    Your a professional bank robber, about to rob the Grand National Bank for £100 million.
    You must pick a partner, choose the right equipment, make the right choices in high action situations,
    to pull of the heist of the century!
    """)
    
def exitGame():
    #Displays exit message
    print()
    print("You successfully pulled of the heist of the century",
          "\nThanks for playing!")

#main
health = 0
game_score = 0
hostage_death = 0
IsUziEquipped = False
IsPistolEquipped = False
IsArmourLEquipped = False
IsArmourHEquipped = False
IsC4Equipped = False
IsDrillEquipped = False
while(True):
    titleScreen()
    
    

        
