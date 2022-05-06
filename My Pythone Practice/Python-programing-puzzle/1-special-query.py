
list = [1,2,3, 19,19, 5,5,5,5,5, "ads"]

def checkIntList(list):
    try:
        for i in list:
            int(i)
        return True
    except:
        return False


if checkIntList(list):
    count_5 = list.count(5)
    count_19 = list.count(19)
    if count_19 == 2 and count_5 >= 3:
        print("True") 
    else: 
        print("False")
else: 
    print("Not integer")
