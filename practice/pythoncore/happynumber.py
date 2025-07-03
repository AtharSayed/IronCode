def isHappy(n):
  seen = set()
  while n!=1:
    if n in seen:
      return False
    digit_list = list(map(int,str(n)))
    square_list = [x**2 for x in digit_list]
    n = sum(square_list)
  return True 

if __name__ == "__main__":
  n = int(input("Enter the number :))
  res = isHappy(n)
  print(res)
