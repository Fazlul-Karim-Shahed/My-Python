y = []      # init a matrix
for i in range(5):
    y.append([int(x) for x in input().split()])    #


for k in range(5):
    z = len(y[k])
    for n in range(z):
        if y[k][n] == 1:
            print(f"{abs(2-k) + abs(2-n)}")