class bank:
	def __init__(self,a,n,t):
		self.acc=a
		self.name=n
		self.acc_type=t
		self.balance=0
	def deposite(self):
		new=float(input("enter the amount to be deposite:"))
		self.balance=self.balance+new
	def withdraw(self):
		new=float(input("enter the amount you want to withdraw:"))
		if new>self.balance:
			print("required withdrawal money is not available in your account:")
		else:
			self.balance=self.balance-new
	def viewbalance(self):
		print("balance amount available at your account is:",self.balance)
a=int(input("enter your account number:"))
n=input("enter your account name:")
t=input("enter your account type:")
acc=bank(a,n,t)
c=0

while(c<4):
	print("\n1.deposite\n2.withdraw\n3.view balance\n4.exit")
	c=int(input("enter your choice:"))
	if c==1:
		acc.deposite()
	elif c==2:
		acc.withdraw()
	elif c==3:
		acc.viewbalance()
	elif c==4:
		break
	else:
		print("invalid choice")
		
