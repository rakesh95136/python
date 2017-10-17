class employee:
	
	amount = 0
	

		
	def __init__(self,first,last,sal):
		self.first = first
		self.last = last
		self.sal = sal


	def fun1(self):
		self.sal = 333
		b = 'TMMMMM'
		return self.sal,b

	def fun2(self):
		pass

	@classmethod
	def c1(cls,amount):
		cls.amount = amount

	@classmethod
	def c2(cls,str):
		first,last,sal = str.split('-')
		return cls(first,last,sal)


a1 = 'rakesh-thakur-3000'
b1 = 'kola-totka-2000'


e1 = employee.c2(b1)

print(e1.first)




