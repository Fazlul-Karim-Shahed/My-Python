

list = ['a', 'abb', 'sfs', 'oo', 'de', 'sfde']

def checkList(list, position):
    if list[position].count(list[position-1]):
        return True
    else: return False

print(checkList(list, 4))
