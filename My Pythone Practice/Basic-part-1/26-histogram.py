
def histogram(list):
    for i in list:
        print(i)
        print("*" * i)

userList = input()
list = userList.split(",")

for i in range(len(list)):
    list[i] = int(list[i])

print(list)
print(histogram(list))