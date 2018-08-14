# Taken from mission The Lancers

# Taken from mission The Vampires

# Taken from mission The Defenders

# Taken from mission Army Battles

# Adding Splash as the Lancer capacity & Needs to redefine fight between unit

# Adding Healing capacity and Max HP. Modifying vampirism so Heal & Vampire use the restro function.

__DEBUG__ = False

def log(text: str):
    if __DEBUG__:
        print(text)

class Warrior:
    def __init__(self):
        self.max_health = 50
        self.health = 50
        self.attack = 5
        self.defense = 0
        self.is_alive = True
        self.vampirism = 0
        self.splash = 0
        self.healpower = 0
        
    def defend(self, attack):
        if attack > self.defense:
            self.health -= (attack - self.defense)
        if self.health <= 0:
            self.is_alive = False

    def restore(self, life):
        self.health = min(self.max_health, self.health +life)     

class Knight(Warrior):
    def __init__(self):
        self.max_health = 50
        self.health = 50
        self.attack = 7
        self.defense = 0
        self.is_alive = True
        self.vampirism = 0
        self.splash = 0
        self.healpower = 0
        
class Defender(Warrior):
    def __init__(self):
        self.max_health = 60
        self.health = 60
        self.attack = 3
        self.defense = 2
        self.is_alive = True
        self.vampirism = 0
        self.splash = 0
        self.healpower = 0

class Vampire(Warrior):
     def __init__(self):
        self.max_health = 40
        self.health = 40
        self.attack = 4
        self.defense = 0
        self.is_alive = True
        self.vampirism = 0.5
        self.splash = 0
        self.healpower = 0

class Lancer(Warrior):
     def __init__(self):
        self.max_health = 50
        self.health = 50
        self.attack = 6
        self.defense = 0
        self.is_alive = True
        self.vampirism = 0
        self.splash = 0.5
        self.healpower = 0

class Healer(Warrior):
    def __init__(self):
        self.max_health = 60
        self.health = 60
        self.attack = 0
        self.defense = 0
        self.is_alive = True
        self.vampirism = 0
        self.splash = 0
        self.healpower = 2
    
    def heal(self, unit):
        unit.restore(self.healpower)

class Army:
    
    def __init__(self):
        self.Units = []
        self.size = 0
        self.firstAlive = 0
        self.allDead = False

    def add_units(self, UnitType, number):
        for i in range(number):
            unit = UnitType()
            self.Units.append(unit)
        self.size += number

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
    turn = 1
    while unit_1.is_alive:
        if not unit_2.is_alive:
            return True
        if turn % 2 == 0:
            unit_1.defend(unit_2.attack)
            if unit_2.vampirism > 0:
                unit_2.restore((unit_2.attack-unit_1.defense)*unit_2.vampirism)
            if unit_2.splash > 0:
                if next_unit_1 :
                    next_unit_1.health -= (unit_2.attack-unit_1.defense)*unit_2.splash
            if next_unit_2 and next_unit_2.healpower >0:
                next_unit_2.heal(unit_2)                
        else:
            unit_2.defend(unit_1.attack)
            if unit_1.vampirism > 0:
                unit_1.restore((unit_1.attack-unit_2.defense)*unit_1.vampirism)
            if unit_1.splash > 0:
                if next_unit_2:
                    next_unit_2.health -= (unit_1.attack-unit_2.defense)*unit_1.splash
            if next_unit_1 and next_unit_1.healpower >0:
                next_unit_1.heal(unit_1)                   

        turn += 1
        log("Unit1:="+str(unit_1.health))
        log("Unit2:="+str(unit_2.health))
    return False



def fight(unit_1, unit_2):
    #This is one to one battle no need to implement Splash
    turn = 1
    while unit_1.is_alive:
        if not unit_2.is_alive:
            return True
        if turn % 2 == 0:
            unit_1.defend(unit_2.attack)
            if unit_2.vampirism > 0:
                unit_2.health += (unit_2.attack-unit_1.defense)*unit_2.vampirism
        else:
            unit_2.defend(unit_1.attack)
            if unit_1.vampirism > 0:
                unit_1.health += (unit_1.attack-unit_2.defense)*unit_1.vampirism

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