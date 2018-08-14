# Taken from mission Army Battles

__DEBUG__ = False

def log(text: str):
    if __DEBUG__:
        print(text)

class Warrior:
    def __init__(self):
        self.health = 50
        self.attack = 5
        self.defense = 0
        self.is_alive = True
        
    def defend(self, attack):
        if attack > self.defense:
            self.health -= (attack - self.defense)
        if self.health <= 0:
            self.is_alive = False

class Knight(Warrior):
    def __init__(self):
        self.health = 50
        self.attack = 7
        self.defense = 0
        self.is_alive = True
        
class Defender(Warrior):
    def __init__(self):
        self.health = 60
        self.attack = 3
        self.defense = 2
        self.is_alive = True    

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
            if fight(army1.Units[army1.firstAlive], army2.Units[army2.firstAlive]):
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


def fight(unit_1, unit_2):
    turn = 1
    while unit_1.is_alive:
        if not unit_2.is_alive:
            return True
        if turn % 2 == 0:
            unit_1.defend(unit_2.attack)
        else:
            unit_2.defend(unit_1.attack)
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

    #battle tests
    my_army = Army()
    my_army.add_units(Defender, 1)
    
    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Defender, 1)

    army_4 = Army()
    army_4.add_units(Warrior, 2)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == False
    assert battle.fight(army_3, army_4) == True
    print("Coding complete? Let's try tests!")
