#PYTHON NUMBERS
#Example
x = 1
y = 2.8
z = 1j
                    #output
print(type(x))      #<class 'int'>
print(type(y))      #<class 'float'>
print(type(z))      #<class 'complex'>
                    

#Example int
x = 1
y = 35656222554887711
z = -3255522
                   #output
print(type(x))     #<class 'int'>
print(type(y))     #<class 'int'>
print(type(z))     #<class 'int'>


#Example floats
x = 1.10
y = 1.0
z = -35.59
                  #output
print(type(x))    #<class 'float'>
print(type(y))    #<class 'float'>
print(type(z))    #<class 'float'>

#Example2
x = 35e3
y = 12E4
z = -87.7e100
                  #output
print(type(x))    #<class 'float'>
print(type(y))    #<class 'float'>
print(type(z))    #<class 'float'>


#Example complex
x = 3+5j
y = 5j
z = -5j
                  #output
print(type(x))    #<class 'complex'>
print(type(y))    #<class 'complex'>
print(type(z))    #<class 'complex'>


#Example Type Conversion
#convert from int to float:
x = float(1)

#convert from float to int:
y = int(2.8)

#convert from int to complex:
z = complex(1)
                   #output
print(x)           #1.0
print(y)           #2
print(z)           #(1+0j)

print(type(x))     #<class 'float'>
print(type(y))     #<class 'int'>
print(type(z))     #<class 'complex'>


#Example Random Number
import random

print(random.randrange(1, 10))
#output: 6 

