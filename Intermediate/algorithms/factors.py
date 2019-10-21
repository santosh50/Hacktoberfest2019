#Factors of a number
from math import sqrt
n = int(input("Enter a number: "))
print(n,'=')
count = 0
for i in range(1,int(sqrt(n))+1):
    if n%i==0:
        print(i,'x',n//i)
        count+=1
if i==n//i:
    print("Number of factors =",(count*2)-1)
else:
    print("Number of factors =",(count*2))


        

