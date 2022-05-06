x = [int(i) for i in input().split()]
tar = int(input("Target : "))
l = len(x)
count = 0
for i in range(0,l,1):
    for j in range(0,l,1):
        if x[i] + x[j] == tar :
            print("x[%d] + x[%d] = %d + %d = %d" % (i+1, j+1, x[i], x[j], tar))
            count=+1
            break
    if count == 1:
        break