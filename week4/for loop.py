for i in range (1,11):
  print(i, end= " ")
  a=[10,54,78,74,85,74,84,114,44,55,55,55,55]
count=0
#b=int(input("enter b = "))
for i in range (0,15):
    if a[i]==55:
        count=count+1

print(f"the count is {count}")
