# Special words are the letters with both low and upp appearance in the word

def special(word):
    count=0
    lower =[]
    upper = []
    for letters in word:
        if letters.islower():
            lower.append(letters)
        else:
            upper.append(letters)
    ups = str(upper).lower()
    lws = set(lower)
    ups = set(ups)
    cmb = lws & ups

    return len(cmb)


if __name__ =="__main__":
    word = input("Enter the words: ")
    result = special(word)
    print(result)





