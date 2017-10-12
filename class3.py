class employee:
	
	s1 = 1
	count = 0
	amount = 0
	def __init__(self,first,last,sal):
		self.first = first
		self.last = last
		self.sal = sal
		employee.count += 1

	def fun1(self):
		self.first = 'Mohan'
		name1 = 'Kota'
		return self.first,name1

	def fun2(self):
		pass

	@classmethod
	def more(cls,amount):
		cls.amount  = amount
		return amount
		
		



e1 = employee('Rakesh','Thakur', 40000)
e2 = employee('Bila', 'Toolk', 40909)


v = employee.more(1000)
print(v)
