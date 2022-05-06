

import random
import string

# str = list(range("a","z"))


lst = list(string.ascii_letters) + list(str([1,2,3,4,5,6,7,8,9,0]))

letterList = random.choices(lst, k=200)

str = ""
for i in range(len(letterList)):
    str += letterList[i]
    
print(str)

list1 = []
