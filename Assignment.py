## New Assignment
ten = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety","hundred"]
for x in range(101):
  if (x%10 == 0) :
      print(ten[x//10])
  else :
    print(x)