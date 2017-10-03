#Define a tuple which contains a string value.When queried, the tuple should be type 'class tuple'
t = ("hello")
print(type(t))  #The type will be string
# Result <class 'str'>


#Define a tuple which contains a string value. When queried, the tuple should of type 'class tuple'
t = ("hello",)
print(type(t))  #The type will be tuple, because it thinks there will be another element after comma
# Result <class 'tuple'>

#Can we define a tuple without the conventional usuage of the parathesis?
#you can define tuple without paranthesis also.
t = "hello",
print(type(t))
# Result <class 'tuple'>