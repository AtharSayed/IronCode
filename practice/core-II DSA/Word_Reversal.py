# Reversing Word in a string 
def reversestring(s):
    words = s.split()
    rev = []
    for word in reversed(words):
        rev.append(word)
    rev = " ".join(rev)
    return rev
if __name__ =="__main__":
    s = "the sky is blue"
    res = reversestring(s)
    print(res)
