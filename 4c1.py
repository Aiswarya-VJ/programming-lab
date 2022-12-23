class rectangle:
	def __init__(self,length,breadth):
		self.length=length
		self.breadth=breadth
	
	def perimeter(self):
		print("perimeter of rectangle=",2*(self.length+self.breadth))
	
	def area(self):
	
		return((self.length)*(self.breadth))
rec1=rectangle(int(input("enter the length of rectangle1:")),(int(input("enter the breadth of rectangle1:"))))
print(rec1.area())
rec2=rectangle(int(input("enter the length of rectangle2:")),(int(input("enter the breadth of rectangle2:"))))
print(rec2.area())

if rec1.area()>rec2.area():
	print("rectangle1 is greater")
else:
	print("rectangle2 is greater")
