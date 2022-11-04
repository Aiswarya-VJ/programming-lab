d2={}
a=input("enter the sentence:").split(" ")
for i in a:
	c=0
	for j in a:
		if i==j:
			c+=1
	d2[i]=c
print(d2)
