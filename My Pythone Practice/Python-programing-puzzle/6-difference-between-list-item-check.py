
my_list = [1,2,3,4,5,6,7,8,9]

def checkList(list):
    count = 0
    for i in range(len(list)):
        if i+1 >= len(list): break
        if abs((list[i] - list[i+1])) == 1: #difference 1
            count = 0
        else:
            return False
    return True

print(checkList(my_list))