#Example PYTHON VARIABLES
x = 5          
y = "Symbat"      #output:
print(x)        #5
print(y)        #Symbat


x = 4       # x is of type int
x = "Symbat" # x is now of type str
print(x)
#output: Symbat

#тип
x = str(3)   
y = int(3)   
z = float(3) 

           #output:
print(x)   #3
print(y)   #3
print(z)   #3.0

#узнать тип
x = 5
y = "Symbat"
print(type(x))
print(type(y))
#output: <class 'int'>
#        <class 'str'>

x = "Symbat"
print(x)
#double quotes are the same as single quotes:
x = 'Symbat'
print(x)
#output: Symbat
#        Symbat


a = 4
A = "Symbat"

print(a)
print(A)
#output 4
#       Symbat



#VARIABLE NAMES
#Example         
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
                 #output
print(myvar)     #John
print(my_var)    #John
print(_my_var)   #John
print(myVar)     #John
print(MYVAR)     #John
print(myvar2)    #John

#not correct!
2myvar = "John"
my-var = "John"
my var = "John"


#Camel Case
myVariableName = "John"

#Pascal Case
MyVariableName = "John"

#Snake Case
my_variable_name = "John"



#Assign Multiple Values
#Example
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#output
#Orange
#Banana
#Cherry

#Example
x = y = z = "Orange"   #output:
print(x)               #Orange
print(y)               #Orange
print(z)               #Orange

#Example
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits     #output:
print(x)             #apple
print(y)             #banana
print(z)             #cherry

#Output Variables
#Example
x = "Symbat is beautiful"
print(x)
#output:
#Symbat is beautiful

#Example
x = "Symbat"
y = "is"
z = "beautiful"
print(x, y, z)   #output: Symbat is beautiful

#Example
x = "Symbat "
y = "is "
z = "beautiful"
print(x + y + z)  #output: Symbat is beautiful

#Example
x = 5
y = 10
print(x + y)   #output: 15

#not correct Example!
x = 5
y = "John"
print(x + y)

#we can write like this
x = 5
y = "John"
print(x, y)  #output: 5 John



#Global Variables
#Example
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()
#output: Python is awesome


#Example2
x = "beautiful"

def myfunc():
  x = "smart"
  print("Symbat is " + x)

myfunc()

print("Symbat is " + x)
#output: Symbat is smart
#        Symbat is beautiful


#Example with Global
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
#output: Python is fantastic


#Example, change Global
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
#output: Python is fantastic

