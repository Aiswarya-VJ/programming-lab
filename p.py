a=list(map(int,input("\n enter the list elements:").split()))
c=[]
for i in a:
    if i>=0:
        c.append(i)
       
print (c)

#square of n numbers
a=list(map(int,input("\n enter the list elements:").split()))
y=[x*x for x in a]
print(y)

#vowels in a word
a=list(input("\n enter the word:"))
b=['a','e','i','o','u']
c=[x for x in a if x in b]
print (c)

#ordinal of a word
a=list(input("\n enter the word:"))
y=[ord(x) for x in a]
print (y)


#leap year

b=int(input("enter the ending year:"))

for i in range(2022,b+1):
	if i%4==0:
		if i%100==0:
			if i%400==0:
				print(i)
		else:
			print(i)


