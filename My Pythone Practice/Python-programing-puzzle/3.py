
def checkInt(digit):
    try:
        int(digit)
        return True
    except:
        return False
    

def checkFun(digit):
    if checkInt(digit) and digit>4**4 and digit%34==4:
        return True
    else:
        return False
    
print(checkFun(914))