#Example Modify Strings

#Example upper case
a = "Symbat"
print(a.upper())
#output: SYMBAT

#Example lower case
a = "AmAzInG"
print(a.lower())
#output: amazing

#Example Remove Whitespace
a = " Hello, World! "
print(a.strip())
#output: Hello, World!

#Example Replace String 
a = "Hello, World!"
print(a.replace("H", "J"))
#output: Jello, World!

#Example split string'
a = "Hello, World!"
b = a.split(",")
print(b)
#outpit: ['Hello', ' World!']



#Example String Concatenation
a = "Hello"
b = "World"
c = a + b
print(c)
#output: HelloWorld

#Example2
a = "Hello"
b = "World"
c = a + " " + b
print(c)
#output: Hello World



#Example Format - Strings

#Example string format
age = 17
txt = "My name is Symbat, I am " + age
print(txt)
#it is not correct!

#Example2 it is correct
age = 17
txt = "My name is Symbat, and I am {}"
print(txt.format(age))

#Example3
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price)) 
#output: I want 3 pieces of item 567 for 49.95 dollars.

#Example
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price)) 
#output: I want to pay 49.95 dollars for 3 pieces of item 567



#Example Escape Character

#not correct example!
txt = "We are the so-called "Vikings" from the north."

#correct example
txt = "We are the so-called \"Vikings\" from the north."
#output: We are the so-called "Vikings" from the north.


