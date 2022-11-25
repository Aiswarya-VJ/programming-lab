def pyramid(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j*i,end=" ")
        print("\n")
a=int(input("enter the number of steps of the pyramid ")) 
pyramid(a)