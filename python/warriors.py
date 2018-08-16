# Taken from mission The Lancers

# Taken from mission The Vampires

# Taken from mission The Defenders

# Taken from mission Army Battles

# Adding Splash as the Lancer capacity & Needs to redefine fight between unit

# Adding Healing capacity and Max HP. Modifying vampirism so Heal & Vampire use the restore function.

# Refactoring to be more class consistent. Adding some more debugging

__DEBUG__ = True

def log(text: str):
    if __DEBUG__:
        print(text)

class Warrior:
    def __init__(self,health=50, attack=5, defense=0, vampirism=0, splash=0, healpower=0):
        self.max_health = health
        self.health = self.max_health
        self.attack = attack
        self.defense = defense
        self.vampirism = vampirism
        self.splash = splash
        self.healpower = healpower
        
    def defend(self, attack):
        if attack > self.defense:
            self.health -= (attack - self.defense)

    def restore(self, life):
        self.health = min(self.max_health, self.health +life)     

    def __str__(self) -> str:
        return self.__class__.__name__

    is_alive = property(lambda self: self.health > 0)


class Knight(Warrior):
    def __init__(self):
        super().__init__(attack=7)
        
class Defender(Warrior):
    def __init__(self):
        super().__init__(health=60, attack=3, defense=2)

class Vampire(Warrior):
    def __init__(self):
        super().__init__(health=40, attack=4, vampirism=0.5)

class Lancer(Warrior):
    def __init__(self):
        super().__init__(attack=6, splash=0.5)

class Healer(Warrior):
    def __init__(self):
        super().__init__(health=60, attack=0, healpower=2)

    def heal(self, unit):
        unit.restore(self.healpower)

class Army:
    
    def __init__(self):
        self.Units = []
        self.size = 0
        self.firstAlive = 0
        self.allDead = False

    def add_units(self, UnitType, quantity):
        for i in range(quantity):
            unit = UnitType()
            self.Units.append(unit)
        self.size += quantity

    def nextPlease(self)->bool:
        self.firstAlive +=1
        if self.firstAlive == self.size:
            self.allDead = True
            return False
        else:
            return True
        
class Battle:

    def fight(self, army1, army2):
        log("Starting Battle")
        while not army1.allDead: 
            if army2.allDead: return True
            log("Army1.firstAlive:="+str(army1.firstAlive))
            log("Army2.firstAlive:="+str(army2.firstAlive))     
            if army1.firstAlive + 1 < army1.size:
                next_unit_1 = army1.Units[army1.firstAlive + 1]   
            else:
                next_unit_1 = None
            if army2.firstAlive + 1 < army2.size:
                next_unit_2 = army2.Units[army2.firstAlive + 1]
            else:
                next_unit_2 = None

            if battle_fight(army1.Units[army1.firstAlive], next_unit_1 ,army2.Units[army2.firstAlive], next_unit_2):
                #army1 unit has killed army2 unit
                if not army2.nextPlease(): 
                    return True #army2 is allDead now
                else: 
                    log("One less in army2.")
                    log("HP left army1 unit:="+str(army1.Units[army1.firstAlive].health))
            else:
                #too bad army1 you are dead now
                if not army1.nextPlease(): 
                    return False #Army1 is no more
                else: 
                    log("One less in army1.")      

        return False


def battle_fight(unit_1, next_unit_1, unit_2, next_unit_2):
    #This will allow fighting with splash mechanism
    log("Battle fight between "+str(unit_1)+"&"+str(next_unit_1)+" vs "+str(unit_2)+"&"+str(next_unit_2))
    turn = 1
    while unit_1.is_alive:
        if not unit_2.is_alive:
            return True
        if turn % 2 == 0:
            unit_1.defend(unit_2.attack)
            if unit_2.vampirism > 0:
                log("Vampirism unit2")
                unit_2.restore((unit_2.attack-unit_1.defense)*unit_2.vampirism)
            if unit_2.splash > 0:
                log("Splash unit2")
                if next_unit_1 :
                    next_unit_1.health -= (unit_2.attack-unit_1.defense)*unit_2.splash
            if next_unit_2 and next_unit_2.healpower >0:
                log("Heal unit2")
                next_unit_2.heal(unit_2)                
        else:
            unit_2.defend(unit_1.attack)
            if unit_1.vampirism > 0:
                log("Vampirism Unit1")
                unit_1.restore((unit_1.attack-unit_2.defense)*unit_1.vampirism)
            if unit_1.splash > 0:
                log("Splash Unit1")
                if next_unit_2:
                    next_unit_2.health -= (unit_1.attack-unit_2.defense)*unit_1.splash
            if next_unit_1 and next_unit_1.healpower >0:
                log("Heal unit1")
                next_unit_1.heal(unit_1)                   

        turn += 1
        log("Unit1:="+str(unit_1.health))
        if next_unit_1: log("&next1:="+str(next_unit_1.health))
        log("Unit2:="+str(unit_2.health))
        if next_unit_2: log("&next2:="+str(next_unit_2.health))
    return False



def fight(unit_1, unit_2):
    #This is one to one battle no need to implement Splash
    log(str(unit_1)+" vs "+str(unit_2))
    turn = 1
    while unit_1.is_alive:
        if not unit_2.is_alive:
            return True
        if turn % 2 == 0:
            unit_1.defend(unit_2.attack)
            if unit_2.vampirism > 0:
                unit_2.restore((unit_2.attack-unit_1.defense)*unit_2.vampirism)
        else:
            unit_2.defend(unit_1.attack)
            if unit_1.vampirism > 0:
                unit_1.restore((unit_1.attack-unit_2.defense)*unit_1.vampirism)

        turn += 1
        log("Unit1:="+str(unit_1.health))
        log("Unit2:="+str(unit_2.health))
    return False

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    
    #fight tests
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()
    bob = Defender()
    mike = Knight()
    rog = Warrior()
    lancelot = Defender()
    eric = Vampire()
    adam = Vampire()
    richard = Defender()
    ogre = Warrior()
    freelancer = Lancer()
    vampire = Vampire()
    priest = Healer()

 
    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False
    assert fight(bob, mike) == False
    assert fight(lancelot, rog) == True

    assert fight(eric, richard) == False

    assert fight(ogre, adam) == True
    assert fight(freelancer, vampire) == True
    assert freelancer.is_alive == True
    assert freelancer.health == 14    
    priest.heal(freelancer)
    assert freelancer.health == 16

    #battle tests
    my_army = Army()
    my_army.add_units(Defender, 2)
    my_army.add_units(Healer, 1)
    my_army.add_units(Vampire, 2)
    my_army.add_units(Lancer, 2)
    my_army.add_units(Healer, 1)
    my_army.add_units(Warrior, 1)
    
    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)
    enemy_army.add_units(Lancer, 4)
    enemy_army.add_units(Healer, 1)
    enemy_army.add_units(Defender, 2)
    enemy_army.add_units(Vampire, 3)
    enemy_army.add_units(Healer, 1)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Lancer, 1)
    army_3.add_units(Healer, 1)
    army_3.add_units(Defender, 2)

    army_4 = Army()
    army_4.add_units(Vampire, 3)
    army_4.add_units(Warrior, 1)
    army_4.add_units(Healer, 1)
    army_4.add_units(Lancer, 2)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == False
    assert battle.fight(army_3, army_4) == True

    print("Coding complete? Let's try tests!")