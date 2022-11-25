def fibinocci(n):
    if n<=1:
        return n
    else:
        return(fibinocci(n-1)+fibinocci(n-2))
n=int(input("enter number of terms:"))
print("fibinocci series:")
for i in range(n):
    print(fibinocci(i))
