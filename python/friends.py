__DEBUG__ = True

def log(text: str):
    if __DEBUG__:
        print(text)

def check_connection(network, first, second):

    accessible = []
    unknown = []
    log("network:"+str(network))
    log(first)
    log(second)

#Important thing in this kind of algo is to prevent o(n²)
#So will try to go thru network only once

    for couple in network:
        log(couple)
        if second in accessible:
            return True
            #Stop research if found
            #will occur only if we have a lucky order of pairs 
        log(couple.split("-"))
        friends = couple.split("-")
        if first in friends :
            #We start the friend ring
            if friends[0] not in accessible:
                accessible.append(friends[0])
            if friends[1] not in accessible:
                accessible.append(friends[1])
        if friends[0] in accessible or friends[1] in accessible :
            #We already have some friends in ring
            if friends[0] not in accessible:
                accessible.append(friends[0])
            if friends[1] not in accessible:
                accessible.append(friends[1])
        else:
            #We do not know (yet) this person
            if friends[0] not in unknown:
                unknown.append(friends[0])
            if friends[1] not in unknown:
                unknown.append(friends[1])            
    #We have run thru once, we check again if accessible
    #and then go thru unknown
    if second in accessible:
        return True
    
    for friend in unknown:
        print("We have some work")
    print(accessible)
    print(unknown)
    return False
    
if __name__ == '__main__':
#These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_connection(("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2","scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),"scout2", "scout3") == True, "Scout Brotherhood"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "super", "scout2") == True, "Super Scout"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "dr101", "sscout") == False, "I don't know any scouts."
    
    

