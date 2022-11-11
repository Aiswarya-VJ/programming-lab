num =input("enter integer list:").split()
num =[int(x) for x in num]
num = [x for x in num if x%2!=0]
print(num)
