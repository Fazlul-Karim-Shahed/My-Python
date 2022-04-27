def marks(a):
    assert a>=0 and a<=100 , "Marks must 0 to 100"
    if a>=33:
        print("Pass")
    else:
        print("fail")



try:
    a = int(input("Enter Your Marks : "))
    marks(a)

except (Exception,ZeroDivisionError,ValueError):
    print("Something Wrong")