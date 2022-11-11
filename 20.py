list = [11, 22, 33, 44, 55,66]
print(f"list is:",list)
for i  in list:
	if(i%2 == 0):
	    list.remove(i)
print (f"list after removing even numbers:",list)
