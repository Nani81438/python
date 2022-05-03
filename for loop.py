'''for i in range(10):
    print(i,end = '-')'''

'''for x in range(2, 6,2): # start,end,stepvalue
  print(x)'''

#tables
'''n= int (input ("enter a number"))
for i in range(1,11):
    c = n * i
    print(n,'*', i,'=',c)'''

#Program to print even number using step size in range()
'''n= int (input ("enter a number"))
for i in range (2,n,2):
    print (i)'''


'''list = ['Peter','Joseph','Ricky','Devansh']

for i in list:
    print("Hello", i)'''

#Exit the loop when x is "banana":
'''fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
      break'''

#Exit the loop when x is "banana", but this time the break comes before the print:
'''fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)'''

#With the continue statement we can stop the current iteration of the loop, and continue with the next:
'''fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)'''

#Nested for loop
# User input for number of rows
'''rows = int(input("Enter the rows:"))
# Outer loop will print number of rows
for i in range(0,rows+1):
# Inner loop will print number of Astrisk
    for j in range(i):
        print("*",end = '')
    print()'''

#factorial
'''n = int (input ("enter a number:"))
factorial = 1
if n<0:
    print("number should be positive")
elif n == 0:
    print ("factorial = 1 ")
else:
    for i in range (1,n+1):
        factorial = factorial*i
print ('factorial of the number is : ',factorial)'''

# write a program to print first 10 even numbers in reverse order
'''for x in reversed(range (2,21,2)):
    print (x)'''
# printing a table
'''n = int (input ("enter the number: "))
for i in range (1,11):
    m = n*i
    print (n,'*',i,"=", m )'''

# sum of numbers
# Program to find the sum of all numbers stored in a list

# List of numbers
'''numbers = [1,2,3,4,5,6]

# variable to store the sum
sum = 0

# iterate over the list
for val in numbers:
    sum = sum+val

print("The sum is", sum)'''

# mulplication of digits in a number
'''i = int (input("enter a number: "))
prod = 1
while i>0:
    prod = prod * (i%10)
    i = i // 10
    print (" the product of digits in a number :" ,prod)'''

# ARMSTRONG NUMBER:-number of n digits equal sum of   nth power of n digits
'''for i in range (1001):
    num = i
    result = 0
    n = len(str(i))
    while(i!=0):
        digit = i%10
        result = result+digit**n
        i = i//10
    if num == result:
        print (num)'''
# printing numbers in a triangular shape
'''n = int (input("enter number of rows: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print (j,end="")
    print()'''
#
'''n = int (input("enter number of rows: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print (i,end="")
    print()'''

'''str = "Python"
for i in str:
    print(i) '''
#table
'''list = [1,2,3,4,5,6,7,8,9,10]
n = 5
for i in list:
    c = n*i
    print (c)'''

# Program to print the sum of the given list.
'''list = [1,2,3,4,5,6,7,8,9,10]
sum = 0
for i in list :
    sum+=i
print (" the sum is: ", sum)'''

# printing 1 to 10 numbers
'''for i in range(10):
    print(i, end = ' ') '''














