class employee:
	s = 300
	def __init__(self,first,last,sal):
		self.first = first
		self.last = last
		self.sal = sal

	def fun1(self):
		self.first = 'Different'
		return self.first

	def fun2(self):
		self.sal = 8000
		d = 4 + self.s
		return d

e1 = employee('Rakesh','Thakur',10000)
print(e1.fun2())


		
