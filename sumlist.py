def sumlist(l):
    sum=0
    for i in l:
        sum=sum+i
    return sum
l=list(map(int,input("\n enter the numbers in l1:\n").split()))
print("list is:",l)
print("sum of list:",sumlist(l))
