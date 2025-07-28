def fun(num_rows):
    tot = [[1]]
    for i in range(1,len(num_rows)):
        prev = tot[-1]
        new_row = [1]
        for j in range(1,len(prev)):
            new_row.append(prev[i-j] + prev[j])
        new_row.append(1)
        tot.append(new_row)
    return tot

if __name__ =="__main__":
  numRows = int(input("Enter the number of Rows : "))
  res = fun(numRows)
  print(res)
