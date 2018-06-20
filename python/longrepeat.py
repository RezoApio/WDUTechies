def long_repeat(line):
    """
        length the longest substring that consists of the same char
    """
    import re
    # your code here
    sol = 0 
    for i in range(len(line)):
        sol=max(sol,len(max(re.findall(line[i]+"+",line),key=len)))
        
    return sol

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')
