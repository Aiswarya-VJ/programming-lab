str1=str(input("enter the word"))
list1=list(str1)
print(f"string is:",list1)
print("string after exchanging the first and last characters")
temp=list1[0]
list1[0]=list1[-1]
list1[-1]=temp
print(list1)