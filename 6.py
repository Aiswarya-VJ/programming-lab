a=2022
b=int(input("enter a year"))
if (a<b):
   print("Leap years are : ")
while(a<b):
     if (a%400==0)or(a%100!=0 and a%4==0):
         print(a)
     a+=1