l1=list(map(int,input("\n enter the numbers in l1:\n").split()))
l2=list(map(int,input("\n enter the numbers in l2:\n").split()))
n,m=len(l1),len(l2)
print("length is same:")if m==n else print("length is  not same:")
s1,s2=sum(l1),sum(l2)
print("sum is same")if s1==s2 else print("sum is not same:")
for x in l1:
    for y in l2:
        if x == y:
           print("common element = ",x)
           
           
