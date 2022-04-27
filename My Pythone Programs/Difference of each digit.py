n = input("N = ")
count = 0
for i in n:
    count+=1
for i,j in zip(range(0,count,1),range(1,count,1)):
    x= int(n[j]) - int(n[i])
    print(x,end=" ")
