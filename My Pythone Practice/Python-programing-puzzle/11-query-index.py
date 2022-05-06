
special_list = [(100, (0, 12, 45, 3, 4923, 322, 105, 29, 15, 39, 55))]

def checkList(special_list):
    extract_list = special_list[0][1]
    n = special_list[0][0]
    return [i for i,item in list(enumerate(extract_list)) if item>n]

print(checkList(special_list))
