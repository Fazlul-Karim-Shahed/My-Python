
my_list = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]

def checkList(myList):
    # count = 0
    f = 0
    for k in range(len(myList)):
        l = f + 3
        if l>len(myList): 
            break
        for i in range(f,l+1,1):
            for j in range(f,l+1,1):
                if i!= j:
                    if myList[i] == myList[j]:
                        return False
        f+=4
                    
    return True

print(checkList(my_list))