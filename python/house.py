__DEBUG__ = False

def log(text: str):
    if __DEBUG__:
        print(text)

def house(plan):
    #replace this for solution
    lines=plan.splitlines()
    vert=0
    horiz=0
    #House size is 0 on the 2 dimensions
    log("lines:=")
    log(lines)
    up=0
    bottom=len(lines)
    #Setting up as min value and bottom as max value
    right=0
    left=999
    for j in range(len(lines)):
        line=lines[j]
        log("current line :=: "+line)
        if '#' in line:
            up=max(up,j); log(up)
            bottom=min(bottom,j); log(bottom)
            #same idea setting left as max right and right as max left
            for i in range(len(line)):
                log(line[i])
                if line[i] == '#':
                    left=min(left,i)
                    right=max(right,i)
    horiz=max(right-left+1,0)
    vert=max(up-bottom+1,0)
    log("horiz:="+str(horiz))
    log("vert:="+str(vert))
    return vert*horiz

if __name__ == '__main__':
    assert house('''0000
0000
''') == 0

    assert house("\n00#0\n0#00\n#000\n") == 9 , "3*3"
    assert house("0000##0000\n#000##000#\n##########\n##000000##\n0########0\n") == 50, "house50"
    
    print("Example:")
    print(house('''
0000000
##00##0
######0
##00##0
#0000#0
'''))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert house('''
0000000
##00##0
######0
##00##0
#0000#0
''') == 24

    assert house('''0000000000
#000##000#
##########
##000000##
0000000000
''') == 30

    assert house('''0000
0000
#000
''') == 1


    assert house('''
0##0
0000
#00#
''') == 12

    print("Coding complete? Click 'Check' to earn cool rewards!")
