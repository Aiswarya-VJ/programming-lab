f=open("aaa.txt","r")
l=f.readlines()
l=[x.strip() for x in l]
print(l)

