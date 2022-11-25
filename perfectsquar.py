def even(n):
    for i in str(n):
        if int(i) % 2 ==0:
            pass
        else:
            return False
    return True


a=int(input("enter the range "))
if a>999:
    l1=[]
    for x in range(1000,a,2):
        b1=even(x)
        if (b1==True):
            if ((x**0.5) == int(x**0.5)):
                l1.append(x)
    print(l1)
else:
    print("enter the correct range ")
