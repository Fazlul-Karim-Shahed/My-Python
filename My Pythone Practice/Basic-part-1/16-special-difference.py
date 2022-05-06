

def specialDifference(number):
    constant = 17
    if number > constant:
        return (number - constant)*2
    else:
        return  abs(number - constant)


number = int(input("Enter a number : "))

result = specialDifference(number)

print(result)

