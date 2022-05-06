
list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
tempList = []
removedNumber = 2

for i in range(len(list)):
    if removedNumber >= len(list): 
        removedNumber = 2
    if len(list) == 3:
        tempList.append(list[1])
        list.pop(1)
        tempList.append(list[1])
        list.pop(1)
        tempList.append(list[0])
        break
    tempList.append(list[removedNumber])
    list.pop(removedNumber)
    removedNumber+=2
    print(list)

print(tempList)