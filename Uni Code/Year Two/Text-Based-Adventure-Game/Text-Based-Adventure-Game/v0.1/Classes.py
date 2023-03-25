class Item(object):
    def _init_(self, name, description, value = 0, damage = 0, health = 0, money):
        self.name = name
        self.description = description
        self.value = value
        self.damage = damage
        self.health = health

class player(object):
    def _init_(self, damage, health, money):
        self.damage = 0
        self.health = 100
        self.money = 0
        weapon = 'unarmed'
        armour = 'suit'
        

class hostage(object):
    def _init_(self):
        self.health = 1
        self.damage = 0
    
class policeOfficer(object):
    def _init_(self):
        self.health = 20
        self.damage = 10

class riotPolice(object):
    def _init_(self):
        self.health = 35
        self.damage = 25

def endStats():



inventory = []
IsUziEquipped = False
IsPistolEquipped = False
IsArmourLEquipped = False
IsArmourHEquipped = False
IsC4Equipped = False
IsDrillEquipped = False


def Shop():
    global IsUziEquipped
    global IsPistolEquipped
    global IsArmourLEquipped
    global IsArmourHEquipped
    global IsC4Equipped 
    global IsDrillEquipped
    global inventory
    player.money = 10:
    uzi = Item('Uzi', 'Automatic Submachine Gun', 0, 45, 0,4'k')
    silenced_pistol = Item('Silenced Pistol', 'Semi auto pistol used for stealth', 0, 20,0,6.5'k')
    armour_light = Item('Light Armour','Armour made of a polycarbon fiber',0,0,10,1'k')
    armour_heavy = Item('Heavy Armour','Armour made of Kevlar',0,0,25,2.5'k')
    c4 = Item('C4','Plastic Explosive, good for blowing up things',0,0,0,2'k')
    power_drill = ('Battery Powered Drill','Can drill through steel plates',0,0,0,1.5'k')
    stock = ['1:Uzi', '2:Silenced Pistol', '3:Light Armour', '4:Heavy Armour', '5:C4', '6:Battery Powered Drill']
    option = input("Davey's Dodgy Deals, What do you want: ")
    for stock in stock:
        print(stock)
    def ShopLoop():
        while(True):
            if option = '1':
                if IsUziEquipped == True or IsPistolEquipped == True:
                    print("You Already have a weapon")
                    ShopLoop()
                else:
                    print(uzi[1], 'Sold')
                    IsUziEquipped = True
                    player.money = - 4
                    player.damage += uzi.damage
                    inventory.append(uzi)
                    print("You have", player.money,"k left")
                    
            elif option = '2':
                if IsUziEquipped == True or IsPistolEquipped == True:
                    print("You Already have a weapon")
                    ShopLoop()
                else:
                    print(silenced_pistol[1], 'Sold')
                    IsPistolEquipped = True
                    player.money = - 6.5
                    player.damage += silenced_pistol.damage
                    inventory.append(silenced_pistol)
                    print("You have", player.money,"k left")

            elif option = '3':
                if IsArmourLEquipped == True or IsArmourHEquipped == True:
                    print("You Already have armour")
                    ShopLoop()
                else:
                    print(armour_light[1], 'Sold')
                    IsArmourLEquipped = True
                    player.money = - 1
                    player.health += armour_light.health
                    inventory.append(armour_light)
                    print("You have", player.money,"k left")
                
            elif option = '4':
                if IsArmourLEquipped == True or IsArmourHEquipped == True:
                    print("You Already have armour")
                    ShopLoop()
                else:
                    print(armour_heavy[1], 'Sold')
                    IsArmourHEquipped = True
                    player.money = - 2.5
                    player.health += armour_heavy.health
                    inventory.append(armour_heavy)
                    print("You have", player.money,"k left")

                
            elif option = '5':
                if IsC4Equipped == True or IsDrillEquipped == True:
                    print("You Already have equipment")
                    ShopLoop()
                else:
                    print(c4[1], 'Sold')
                    IsC4Equipped = True
                    player.money = - 2
                    inventory.append(c4)
                    print("You have", player.money,"k left")
                    
            elif option = '6':
                if IsC4Equipped == True or IsDrillEquipped == True:
                    print("You Already have equipment")
                    ShopLoop()
                else:
                    print(power_drill[1], 'Sold')
                     IsDrillEquipped = True
                    player.money = - 1.5
                    inventory.append(power_drill)
                    print("You have", player.money,"k left")
            else:
                print("That's not for sale!")
            decision = input("Is that it(y/n): ")
            if decision = 'y':
                break
        


Shop()
    
