
color_list_1 = {"white", "black", "red"}
color_list_2 = {"purple","white", "blue"}
list = []

for i in color_list_1:
    count = 0
    for j in color_list_2:
        if i == j:
            count = 0
            break
        else:
            count+=1
    if count != 0:
        list.append(i)

print(list)