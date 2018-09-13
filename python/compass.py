__DEBUG__ = False

def log(text: str):
    if __DEBUG__:
        print(text)

class Point:
    def __str__(self):
        return "Point ({},{})".format(self.x, self.y)

    def __init__(self, a, b):
        self.x = a
        self.y = b

    def move(self,dx:int,dy:int):
        return Point(self.x + dx, self.y + dy)

def int_dist(a: Point, b: Point) -> int:
    if a.x == b.x or a.y == b.y :
        dist = abs(a.x - b.x) + abs(a.y - b.y)
        log(dist)
        return dist
        #Horiz or Vert distance
    else:
        #go 1 step in diag and return 1 + int_dist
        if a.x > b.x:
            dx = -1
        else:
            dx = 1
        if a.y > b.y:
            dy = -1
        else:
            dy = 1
        log("dx:="+str(dx))
        log("dy:="+str(dy))
        c = a.move(dx,dy) #cannot move a to prevent wrong values for next distance
        log(c)
        log("1+dist("+str(c)+","+str(b)+")")
        return 1 + int_dist(c,b)
        

def navigation(seaside):
    #replace this for solution
    log(seaside)
    log(len(seaside))

    for rows in range(len(seaside)):
        row=seaside[rows]
        for cols in range(len(row)):
            if row[cols] == 'Y':
                Y=Point(rows,cols)
            elif row[cols] == 'C':
                C=Point(rows,cols)
            elif row[cols] == 'M':
                M=Point(rows,cols)
            elif row[cols] == 'S':
                S=Point(rows,cols)
    
    log("Y:"+str(Y))
    log("M:"+str(M))
    log("S:"+str(S))
    log("C:"+str(C))
    log("calcul ds"); ds = int_dist(Y,S); log("ds:="+str(ds))
    log("calcul dm"); dm = int_dist(Y,M); log("dm:="+str(dm))
    log("calcul dc"); dc = int_dist(Y,C); log("dc:="+str(dc))


    return dm+dc+ds

if __name__ == '__main__':
    print("Example:")
    print(navigation([['Y', 0, 0, 0, 'C'],
                      [ 0,  0, 0, 0,  0],
                      [ 0,  0, 0, 0,  0],
                      ['M', 0, 0, 0, 'S']]))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert navigation([['Y', 0, 0, 0, 'C'],
                       [ 0,  0, 0, 0,  0],
                       [ 0,  0, 0, 0,  0],
                       ['M', 0, 0, 0, 'S']]) == 11

    assert navigation([[ 0,  0, 'C'],
                       [ 0, 'S', 0],
                       ['M','Y', 0]]) == 4

    assert navigation([[ 0,  0, 0,  0,  0,  0,  0],
                       [ 0,  0, 0, 'M', 0, 'S', 0],
                       [ 0,  0, 0,  0,  0,  0,  0],
                       [ 0,  0, 0, 'C', 0,  0,  0],
                       [ 0, 'Y',0,  0,  0,  0,  0],
                       [ 0,  0, 0,  0,  0,  0,  0]]) == 9
    print("Coding complete? Click 'Check' to earn cool rewards!")
