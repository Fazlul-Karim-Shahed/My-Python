
def sum(x,y):
    if isinstance(x, int) and isinstance(y, int):
        return  x+y
    return  "Inputs must be integers!"


print(sum(5,3))