### 1. Write a Python function to find the Max of three numbers.

number1 = float(input('number one add: '))
number2 = float(input('number two add: '))
number3 = float(input('number three add: '))

if (number1>number2) and (number1 > number3):
    maxnumber = number1
elif (number2 > number1) and (number2 > number3):
    maxnumber = number2
else:
    maxnumber = number3
print('max number:',maxnumber)

### 2. Write a Python function to sum all the numbers in a list. 
# Go to the editor Sample List : (8, 2, 3, 0, 7) Expected Output : 20

def cem(mylist):
    x = 0
    for i in mylist:
        x += i
    return x

print(cem((8, 2, 3, 0, 7)))

### 3. Write a Python function to multiply all the numbers in a list. 
# Go to the editor Sample List : (8, 2, 3, -1, 7) Expected Output : -336

def multiply(Sample_list):
    x = 1
    for i in Sample_list:
        x *= i
    return x

print(multiply((8, 2, 3, -1, 7)))

### 4. Write a Python program to reverse a string. 
# Go to the editor Sample String : "1234abcd" Expected Output : "dcba4321"

Sample_String = "1234abcd" [::-1]
print(Sample_String)

### 5. Kvadrat tenliyi hell eden funksiya yazin (Kvadrat tenliyi research edin eger bilmirsize)

import math

def kvadrattenlik(a,b,c):
    D = b * b - 4 * a * c
    sqrt_D = math.sqrt(abs(D))

    if D > 0:
        x1 = ((-b + sqrt_D) / 2 * a)
        x2 = ((-b - sqrt_D) / 2 * a)
        print('tənliyin iki müxtəlif kökü var', x1, 'və', x2)
    elif D == 0:
        x1 = x2 = (-b / 2 * a)
        print('tənliyin iki bərabər kökü var', x1, 'və', x2)
        
    else:
        print("bu Tənliyin real həlli yoxdur ")
        print((-b, '+i', sqrt_D / 2 * a))
        print((-b, '-i', sqrt_D / 2 * a))

a = float(input('1-ci ededi daxil edin: '))
b = float(input('2-ci ededi daxil edin: '))
c = float(input('3-ci ededi daxil edin: '))

if a == 0: 
    print("Kvadrat tenliyi duzgun daxil edin") 
  
else:
    kvadrattenlik(a, b, c)



