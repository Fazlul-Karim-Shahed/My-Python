
def checkIntList(list):
    try:
        for i in list:
            int(i)
        return True
    except:
        return False

def checkFun(list):
    if checkIntList(list):
        length = len(list)
        fifth_element = list[4] 
        if length==8 and list.count(list[4])==3:
            return True
        else: 
            return False
    else:
        return False
    
list = [1,2,3,4,5,5,5,8]
print(checkFun(list))