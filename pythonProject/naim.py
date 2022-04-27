y = [3,1,1,2,1,2,4,3,2,4]
z = [int(n) for n in input().split()]

lenth = len(y)
for i in range(lenth):
    if z[i] == y[i]:
        print(f"{i+1}. Correct")
    else:
        print(f"{i+1}. Wrong. Correct is {y[i]}")