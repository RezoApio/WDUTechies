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
    return False


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

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

    print("Coding complete? Let's try tests!")
