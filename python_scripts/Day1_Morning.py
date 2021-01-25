# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

x=1
print (x)
string="A list of words"
print (string)
monty=True
print (monty)

for i in range (1,11):
    print (i)
    
for i in range (-10,0): 
   print(i)   
   
for i in (1,2,3,4,5,6,7,8,9,10):
    print (i)
  
   
a=1
while a<11:
    print (a)
    a=a+1
    
running=True
number=int(input("Enter a positive integer"))
x=0
while running:
    if number>0:
        print (number)
        print(x)
        x=(number+(number-1))
        number=number-1
    elif number==0:
        break    
print(x)        

number=int(input("Enter a number"))
x=0
for number in range(0,number+1):
    x=x+number
print(x)    
    
                