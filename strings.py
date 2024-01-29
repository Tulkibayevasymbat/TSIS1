#PYTHON STRINGS

#Example           #output:
print("Hello")     #Hello
print('Hello')     #Hello


#Example Assign String to a Variable
a = "Hello"       #output:
print(a)          #Hello


#Example Multiline Strings            #output:
a = """Lorem ipsum dolor sit amet,        
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
#output:
#Lorem ipsum dolor sit amet,
#consectetur adipiscing elit,
#sed do eiusmod tempor incididunt
#ut labore et dolore magna aliqua.


#Example2
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)
#output:
#Lorem ipsum dolor sit amet,
#consectetur adipiscing elit,
#sed do eiusmod tempor incididunt
#ut labore et dolore magna aliqua.


#Example Strings are Arrays
a = "Hello, World!"
print(a[1])
#output: e


#Example Looping Through a String
for x in "sima":
  print(x) 
#output: 
#s
#i
#m
#a


#Example String Length
a = "Sima"
print(len(a))
#output: 4


#Example Check String
txt = "The best things in life are free!"
print("free" in txt)
#output: true

#Example
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
#output: Yes, 'free' is present.


#Example Check if NOT
txt = "The best things in life are free!"
print("expensive" not in txt)
#output: True

#Example
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")
#output: No, 'expensive' is NOT present.


#Example Slicing Strings
b = "Symbat"
print(b[3:5])
#output: bat

#Example
b = "Sima"
print(b[:3])
#output: Sima

#Example Slice To the End
b = "TTulkibayeva"
print(b[1:])
#output: Tulkibayeva

#Example negative indexing
b = "Symbat"
print(b[-5:-1])
#output: ymba

