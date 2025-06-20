def majority(n):
    temp = list(set(n))  
    max_count = 0
    majority_element = None

    for i in range(len(temp)):
        count = n.count(temp[i])
        if count > max_count:
            max_count = count
            majority_element = temp[i]

    return majority_element


if __name__ == "__main__":
    n = [2, 2, 1, 1, 1, 2, 2]
    res = majority(n)
    print(res)
