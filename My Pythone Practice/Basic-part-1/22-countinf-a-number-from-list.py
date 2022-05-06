
def countNumber(list, number):
    count = 0
    for i in list:
        if i == number:
            count = count + 1
    return  count

userList = input("Input numbers with seperated comma: ")
list = userList.split(",")

for i in range(len(list)):
    list[i] = int(list[i])

print(countNumber(list, 4))