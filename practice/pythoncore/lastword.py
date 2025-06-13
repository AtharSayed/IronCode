# To count the length of the last word

def elements(n):
    count = 0
    found_word = False
    for ch in reversed(n):
        if ch !=" " or ch.isalpha():
            count+=1
            found_word = True
        elif found_word:
            break
    return count

if __name__=="__main__":
    try:
        n = input("Enter the words:  ")
        res = elements(n)
        print(res)
    except ValueError:
        print("Enter a valid word and try again !")