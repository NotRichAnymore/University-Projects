import sys
import random
import pygame
import shelve

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
