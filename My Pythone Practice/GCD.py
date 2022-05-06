x = int(input("X = "))
y = int(input("Y = "))

for i in range(1, y+1, 1):
    if x % i == 0 and y % i == 0:
            result = i
print(result)