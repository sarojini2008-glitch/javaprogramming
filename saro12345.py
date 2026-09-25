n=int(input("Enter the start value:"))
s=int(input("Enter the ending value:"))
for i in range(n,s):
    if (i%7==0 or i%5==0):
        continue
    else:
        print(i)
        
