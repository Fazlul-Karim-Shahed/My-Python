x = [int(n) for n in input()]            #input some intiger number
count1 = 0         # init a variable
count0 = 0   # Init a variable

# Counting "1". the count of one is more than or equal 7 usingh loop.
for i in x:               # passing value of x in i.
    if i == 1:
        count1 = count1 +1
    if i == 0:
        count1 = 0
    if count1 >= 7:          # if the count of 1 is more than or equal 7, then stop the loop.
        break
# Counting "0". the count of zero is more than or equal 7 usingh loop.
for i in x:        # passing value of x in i.
    if i == 0:
        count0 = count0 +1
    if i == 1:
        count0 = 0
    if count0 >= 7:  # if the count of zero is more than or equal of 7, then stop the loop
        break

if count0 >= 7:
    print(f"YES")
elif count1 >= 7:
    print(f"YES")
else:
    print(f"NO")
