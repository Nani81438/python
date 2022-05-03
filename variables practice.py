'''a = "hello"
print(a)'''

'''a = "Hello, World!"
print(a[1])'''

#length of a string
'''a = "Hello, World!"
print(len(a))'''

'''txt = "The best things in life are free!"
print("free" in txt)'''

'''txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")'''

'''txt = "The best things in life are free!"
print("expensive" not in txt)'''

'''b = "Hello, World!"
print(b[2:5])'''

'''b = "Hello, World!"
print(b[:5])'''

# slice to till the end
'''b = "Hello, World!"
print(b[2:])'''

# negative indexing
'''b = "Hello, World!"
print(b[-5:-2])'''

# modifying strings
'''a = "Hello, World!"
print(a.upper())'''

'''a = "Hello, World!"
print(a.lower())'''

# for removing white spaces
'''a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"'''

# for replacing
'''a = "Hello, World!"
print(a.replace("H", "J"))'''

# splitting
'''a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']'''

# STRING METHODS
a = "i am good boy!"
#print(a.capitalize()) #converts first character to upper case
#print(a.casefold())# lower the dirst character
#print(a.center()) # returns center character of a string
#printa.count())

# print (a.encode())#Returns an encoded version of the string

s = '    hello  ' .strip() # removes the front and rear extra spaces
print (s)

s = 'www.example.com'.strip('comw.')
print (s)

s = '    hello  ' .lstrip() # removes the left extra spaces
print (s)

s = '    hello  ' .rstrip() # removes the right extra spaces
print(s)

s = 'arthur : three!'.removeprefix('arthur:')
print(s)

s = 'arthur : three!'.lstrip('arthur :')
print(s)

s = "HElloPython".removesuffix('Python')
print(s)

s = "string methods in python".replace(" ","-")
print(s)

s = "string methods in python".replace(" ","")
print(s)

s = "string methods in python".split()
print(s)

list_of_strings = ['string','methods','in','python']
s ='-'.join(list_of_strings)
print(s)

s = 'python is awesome'.upper()
print(s)

s = 'python is awesome'.lower()
print(s)

s = 'python is awesome'.capitalize()
print(s)

print('PYTHON IS AWESOME'.islower())
print('PYTHON IS AWESOME'.islower())
print('PYTHON IS AWESOME'.isupper())

s = 'python'
print (s.isalpha(),s.isalnum(),s.isnumeric())

s = 'hello world'.count('o')
print (s)

s = "machine learning"
idx = s.find('a')
print (idx)
print (s[idx:])

s = "machine learning"
idx = s.rfind("a")
print (idx)
print (s[idx:])

print ("prasannakumar".startswith('p'))
print ("prasannakumar".endswith('r'))

s = "python is awesome!"
parts = s.partition('is')
print (parts)

s = "python is awesome!"
parts = s.center(30,'-')
print (parts)

s = 'heLLo WOrld'
s = s.swapcase()
print (s)

s = '42'.zfill(5)
print (s)

s = 'heLLo WOrld'
s = s.isdigit()
print (s)

s = 'heLLo WOrld'
s = s.isprintable()
print (s)

s = 'heLLo WOrld'
s = s.isspace()
print (s)

s = 'heLLo WOrld'
s = s.isascii()
print (s)







