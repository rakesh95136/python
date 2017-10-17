class employee:
	
	count = 0
	i = 50
	amount1 = 0

	def __init__(self,first,last,sal):
		print("YES : 1")
		self.first = first
		self.last = last
		self.sal = sal
		employee.count += 1
		

	def fun1(self):
		sal1 = self.sal + 1000
		return sal1

	def fun2(self):
		return employee.i


	@classmethod
	def class1(cls,amount):
		return cls(first)

	@classmethod
	def fun2(cls, a):
		ee = a
		return ee

#c = employee.class1(66)
#e1 = employee('Rakesh','Thakur',3000)
#print(e1.last)

d = employee.fun2(33)
print(d)








