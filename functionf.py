def factorial(a):
    f=1
    for i in range(1,a+1):
    	f=f*i
    return(f)
a=int(input("enter a number:"))
b=factorial(a)
print("factorial of",a,"is:",b)
