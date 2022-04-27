line = int(input())
result = []

for i in range(line):
    room = int(input())
    x = input()
    m = max(x.count('R'),x.count('G'),x.count('B'))
    result.append(room-m)

for i in result:
    print(i)