taka =  [500,100,50,20,10,5,2]
poisa = [.9999,.49999,.249999,.099999,.0499999,.0199999,.0099999]
x=float(input("Taka : "))
l1 = len(taka)
l2 = len(poisa)
# finding taka..........

for i in range(0,l1,1):
    n = x// taka[i]
    r = x%taka[i]
    x=r
    print("%d taka need %d"%(taka[i],n))
for i in range(0,l2,1):
    n = x// poisa[i]
    r = x%poisa[i]
    x=r
    print("%.2f poisa need %d"%(poisa[i],n))