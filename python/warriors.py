__DEBUG__ = False

def log(text: str):
    if __DEBUG__:
        print(text)

class Warrior:
    def __init__(self):
        self.health = 50
        self.attack = 5
        self.is_alive = True
        
    def defend(self, attack):
        self.health -= attack
        if self.health <= 0:
            self.is_alive = False

class Knight(Warrior):
    def __init__(self):
        self.health = 50
        self.attack = 7
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

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False

    log("Battle level")
    #battle tests
    my_army = Army()
    my_army.add_units(Knight, 3)
    
    enemy_army = Army()
    enemy_army.add_units(Warrior, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 20)
    army_3.add_units(Knight, 5)
    
    army_4 = Army()
    army_4.add_units(Warrior, 30)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == True
    assert battle.fight(army_3, army_4) == False
    print("Coding complete? Let's try tests!")
