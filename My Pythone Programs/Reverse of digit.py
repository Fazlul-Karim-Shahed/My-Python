x = input("X = ")
count = 0
sum = 0
for i in x:
    count+=1
print("%d" %count)
y = int(x)
for i in range(0,count,1):
    d = y//10
    r = y%10
    y=d
#Reverse
    sum = sum*10 + r
print("%d"%sum)

if sum==int(x):
    print("Palindrome Number")
else :
    print("Not")