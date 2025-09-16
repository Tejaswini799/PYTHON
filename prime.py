'''n=int(input("enter the number"))
c=0
for i in range(2,1):
    if(a%i==0):
        c=c+1
if(c==0):'''
a=int(input("enter lower range"))
b=int(input("enter upper range"))
for i in range(a,b+1):
    count=0
    for j in range(2,i):
        if(i%j==0):
            count=count+1
    if(count==0):
        print(i,end="\n")







