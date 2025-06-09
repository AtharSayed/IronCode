# Greatest English Letter The upper case letter with the highest rank and which has both upper and lowercase appearance is returned in this 
def special(word):
    lower = set()
    upper = set()
    atoz_map_upper = {chr(i): i - 64 for i in range(65, 91)}

    for letter in word:
        if letter.islower():
            lower.add(letter.upper())
        elif letter.isupper():
            upper.add(letter)
    cmb = lower & upper

    if not cmb:
        return ""

    highest = max(cmb, key=lambda x: atoz_map_upper[x])
    return highest

if __name__ =="__main__":
    word = input("Enter the words: ")
    result = special(word)
    print(result)





