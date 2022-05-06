
def changeString(str):
    if(str[:2] == "Is"):
        return  str
    return "Is" + str


str = input()
res = changeString(str)
print(res)