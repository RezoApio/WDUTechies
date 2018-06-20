def checkio(expression):
    #Checking like I would do it opening brackets add 1 to the correct var 
    #no closind allowed while 
    brack = 0
    paren = 0
    brace = 0
    current = ""
    print(expression)

    for index in range(len(expression)):

        if expression[index] == '(':
            paren += 1
            current = current + "p"
            print("(:" + current)

        if expression[index] == '[':
            brack += 1
            current = current + "k"
            print("[:"+ current)

        if expression[index] == '{':
            brace += 1
            current = current + "b"
            print("{:"+ current)

        if expression[index] == ')':
            if len(current) == 0: 
                return False #Never Opened - cannot close 
            print("):"+current[-1])

            if current[-1] == "p": 
                paren -= 1
                print(current)
                current = current[:-1]
                print(current)
            else:
                return False

        if expression[index] == ']':
            if len(current) == 0: 
                return False #Never Opened - cannot close 
            print("]:"+current[-1])

            if current[-1] == "k": 
                brack -= 1
                print(current)
                current = current[:-1]
                print(current)
            else:
                return False
   
        if expression[index] == '}':
            if len(current) == 0: 
                return False #Never Opened - cannot close 
            print("]:"+current[-1])

            if current[-1] == "b": 
                brace -= 1
                print(current)
                current = current[:-1]
                print(current)
            else:
                return False

    if paren == 0 and brace == 0 and brack == 0:
        return True
    else: return False


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("(((1+(1+1))))]") == False, "Failed Once"
    assert checkio("((5+3)*2+1)") == True, "Simple"
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio("2+3") == True, "No brackets, no problem"
    print("ok")
