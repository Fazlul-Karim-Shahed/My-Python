
x = 336
y = 360

def gcd(x,y):
    gcd = 0
    for i in range(1, x):
        if x % i == 0 and y % i == 0:
            gcd = i
    return gcd

def lcm(x,y):
    GCD = gcd(x,y)
    return  (x*y)/GCD

print("GCD: %i" %gcd(360, 336))
print("LCM: %i"%lcm(360, 336))

