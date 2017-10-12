class Employee:
	f = 8
	def __init__(self,first,last,email):
		print("__init__")
		self.first = first
		self.last = last
		self.email = email

	def fun1(self):
		return self.first

	def fun2(self):
		pass

e1 = Employee('rakesh','thakur','dd')
e2 = Employee('leena','katoch','dd')
#e.fun1()
#e.fun2()

print(Employee.fun1(e2))
