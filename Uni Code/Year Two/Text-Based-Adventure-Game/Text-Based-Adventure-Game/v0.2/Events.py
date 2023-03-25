import sys
import Characters
import Menu
import Stages
import random
import pygame
import shelve

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
                      
                            
