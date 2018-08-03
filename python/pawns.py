def safe_pawns(pawns: set) -> int:

    safe =0

    for p in pawns:
        col=p[0]
        row=p[1]

        if int(row) > 1:
            saferow=chr(ord(row)-1)
            #pawn must be below to guard
            if col == "a":
                #only one guard possible
                safecol=chr(ord(col)+1)
                if safecol+saferow in pawns:
                    safe +=1
            elif col == "h":
                 #only one guard possible
                safecol=chr(ord(col)-1)
                if safecol+saferow in pawns:
                    safe +=1
            else:
                safecol1=chr(ord(col)-1)
                safecol2=chr(ord(col)+1)
                if safecol1+saferow in pawns or safecol2+saferow in pawns:
                    safe +=1

    return safe

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")