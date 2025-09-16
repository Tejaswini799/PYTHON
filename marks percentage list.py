a=["SITA","RAVI","GEETHA","TEJA"]
MARKS=[[45,67,45,98],[45,56,78,65],[67,45,87,45],[67,54,87,90]]
per=[]
for i in MARKS:     
    d=sum(i)//4
    per.append(d)
for i in range(4):
   # print("{}. {}: {}%".format(i+1,a[i],per[i]))
    
    print(i+1,a[i],per[i]) 
    
