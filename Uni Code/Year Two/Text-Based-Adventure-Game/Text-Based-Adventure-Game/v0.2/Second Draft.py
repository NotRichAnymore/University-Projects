import sys
import Characters
import Events
import Menu
import Stages
import random
import pygame
import shelve

#Classes for the player, enemies and pickups
from Characters import Item, player, hostage, policeOfficer, riotPolice
from Menu import titleScreen, continueGame, highScores,  how_to_play, exitGame
from Stages import newGame, planStage, startStage1, startStage2, bankStage, vaultStage, moneyStage1, moneyStage2, exitStage1, exitStage2 
from Events import raid, Shop



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
    
    

        
