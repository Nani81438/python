# Requirement:
# steps :
# state = data type
# behaviour = buisiness logical implementation
# validation = testing

'''
x = float(input(" Enter the amount :"))
if x >= 10000:
    print(" your booking confirmed in the flight AR00012 with BUISINESS CLASS ")
elif x >= 5000:
    print(" your booking confirmed in the flight AR00012 with EXECUTIVE CLASS ")
elif x >= 2000:
    print(" your booking confirmed in the flight AR00012 with ECONOMY CLASS ")
else:
    print(" your booking not confirmed in the flight AR00012 ")
'''
# Bus pass

# Requirement: deluxe pass = 1190
# metro pass = 1090
# ordinary pass = 990
# student pass = 650
'''
x = int(input("Enter the amount :"))
if x < 649 or x >= 1191:
    print("Enter valid amount :")
if x >= 1190:
    print("Deluxe pass")
elif x >= 1090:
    print("Metro express pass")
elif x >= 990:
    print("ordinary pass")
elif x >= 650:
    print("student pass")
else:
    print("no pass")'''

# mobile phone purchase in a shop
'''
x = int(input("Enter your purchase amount limit :"))
if (x <= 50000) and (x >= 40000):
    print("select iPHONE models")
elif (x <= 40000) and (x >= 30000):
    print(" select ONE PLUS models")
elif (x <= 30000) and (x >= 20000):
    print("select SAMSUNG models")
elif (x <= 20000) and (x >= 10000):
    print("Select HONOR, OPPO, MI models")
else:
    print(" HAVE A NICE DAY , not available in your range")'''

# Requirement
# sofa = 250
# Balcony = 200
# lounge = 100
'''
y = int(input("Enter the amount you have :"))

if y >= 250:
    print("Get your Premium Lounge ticket")
elif y >= 200:
    print(" Get your Balcony ticket")
elif y >= 150:
    print("Get your Lounge ticket")
else:
    print("No ticket ")'''

#problem 1
'''a=int (input ("enter total no.of working days"))
b=int (input ("enter total no. of days absent"))
percentage = b/a*100
if percentage <75:
    print (" you are not able to sit in the class ")
else:
    print ("you can sit in the class")'''


#problem 2

'''a = int (input("enter the percentage : "))
if a<25:
    print ("you got a  D grade")
elif a>25 and a<45:
    print ("you got a  C grade")
elif a>45 and a<50:
    print ("you got a  B grade")
elif a>50 and a<60:
    print ("you got a  B+ grade")
elif a>60 and a<80:
    print ("you got a  A grade")
else :
    print ("you got a  A+ grade")'''

#problem 3
'''salary= int (input ("what is the salary : "))
period= int (input ("what is your service period : "))
bonus1 = salary * (10/100)
amount1 = bonus1 +salary
bonus2= salary * (8/100)
amount2 = bonus2 +salary
bonus3 = salary * (5/100)
amount3 = bonus3 +salary
if period >10:
    print ("your net bonus amount is : ",amount1 )
elif period >=6 and period<=10:
    print("your net bonus amount is : ",amount2)
elif period <6:
    print("your net bonus amount is: ",amount3)
else:
    print ("sorry you got no bous")'''

#problem 4
mp = int (input (" enter the marked price :"))
if mp>10000:
    print ("pay amount of : ", mp-mp*20/100)
elif mp>7000 and mp<=10000:
    print ("pay amount of : ", mp-mp*15/100)
elif mp<=7000:
    print ("pay amount of : ", mp-mp*10/100)
else:
    print ("sorry you got no discount: ")
print ("thankyou for shopping")

# problem 5
'''
days = int (input (" enter no.of days you used library: "))
if days<=5:
    print ("your charge amount is rupees : ", days*2)
elif days>=6 and days<=10:
    print ("your charge amount is rupees : ", days*3)
elif days>=11 and days<=15:
    print ("your charge amount is rupees : ", days*4)
elif days>15:
    print ("your charge amount is rupees : ", days*5)
else:
    print("you have no charge: ")
print ("thankyou for your usage")
'''




