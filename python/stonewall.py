__DEBUG__ = False

def log(text: str):
    if __DEBUG__:
        print(text)

def stone_wall(wall):
    #replace this for solution
    bricks=wall.splitlines()
    log(bricks)
    lenwall = len(bricks[1]) #Assuming the wall is not empty
    log(lenwall)
    where = [0 for j in range(lenwall)]
    log(where)
    for row in range(len(bricks)-1,0,-1):
        log(bricks[row])
        for col in range(lenwall):
            if bricks[row][col] == '#':
                where[col]+=1 
    
    bomb = 99
    size = 99
    for i in range(len(where)):
        if where[i] < size:
            bomb = i
            size = where[i]
    log(bomb)
    return bomb

if __name__ == '__main__':
    print("Example:")
    print(stone_wall('''
##########
####0##0##
00##0###00
'''))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert stone_wall('''
##########
####0##0##
00##0###00
''') == 4

    assert stone_wall('''
#00#######
#######0##
00######00
''') == 1

    assert stone_wall('''
#####
#####
#####
''') == 0

    print("Coding complete? Click 'Check' to earn cool rewards!")
