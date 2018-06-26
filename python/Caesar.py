def to_encrypt(text, delta):
    #replace this for solution
    ascii_lowera=ord('a')
    ascii_lowerz=ord('z')
    res =""

    for index in range(len(text)):
        if text[index] == ' ':
            res = res + ' '
        else:
            val=ord(text[index]) + delta
            if val < ascii_lowera: 
                val += 26
            elif val > ascii_lowerz:
                val -= 26
            res = res + chr(val)
            
    return res

if __name__ == '__main__':
    print("Example:")
    print(to_encrypt('abc', 10))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert to_encrypt("a b c", 3) == "d e f"
    assert to_encrypt("a b c", -3) == "x y z"
    assert to_encrypt("simple text", 16) == "iycfbu junj"
    assert to_encrypt("important text", 10) == "swzybdkxd dohd"
    assert to_encrypt("state secret", -13) == "fgngr frperg"
    print("Coding complete? Click 'Check' to earn cool rewards!")