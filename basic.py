#This is the very first tutorial in the python
#Here we start with the basic terms


#Datatype:a particular kind of dataitem, as defined by the values it can take,the operations that can be performed on it.
#primitive datatype are implicit in the python . We don't need to declare the variable and its type before using it. All these stuffs is done by the python for us
#SOme of the primitive datatype are int,float,strings

#int
num1=5
num2=10
num3=float(num1+num2)

#we can use type(variable-name) to determine the type of the variable
print(type(num1))
print(type(num2))
print(type(num3))
print(num3)


#float
num1=5.34
num2=10.55
#to convert from float to int, we need to perform explicit type conversion 
num3=int(num1+num2)
print(type(num1))
print(type(num2))
print(type(num3))
print(num3)

#strings
a="Hello welcome to the python tutorials"
print(type(a))

#Note:Every thing in the python are objects. Even the classes ,functions are objects. Default Metaclass(i.e class about the class) of every objects i.e int,float,class,def in python is type. 

#nonprimitive datatypes are list,tuples,sets,dictionary

