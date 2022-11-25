def countch(a):
    c=0
    for i in a:
        if i=='a':
            c=c+1
    return c       
a=input("enter string:")
print("occurence is:",countch(a))
