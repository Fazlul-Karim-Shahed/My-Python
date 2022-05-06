
def sumOfInteger(digit):
    d = digit
    sum = 0
    for i in range(digit):
        r = d%10
        sum = sum + r
        d = int(d/10)

        if d == 0 :
            break
    return  sum

print(sumOfInteger(555))