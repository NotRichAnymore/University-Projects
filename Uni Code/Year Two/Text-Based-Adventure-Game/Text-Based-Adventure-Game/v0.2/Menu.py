import sys
import Characters
import Events
import Menu
import Stages
import random
import pygame
import shelve

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
def continueGame():
    global player
    player = player
    shop()
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
