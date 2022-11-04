d1={}

n=int(input("enter number of items:"))
for i in range(n):
    key=input("enter the key:")
    value=input("enter value;")
    d1[key]=value
d1=sorted(d1.items()) 
print(d1)
d1.sort(reverse=True)
print(d1)

			


     

