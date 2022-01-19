### 1. - Write a Python program to select the odd items of a list.

mylist = [11, 15, 17, 'hello', 'hi', 'string', 90]
print(mylist[::2])

### 2. - Write a Python function to sum all the numbers in a list.
#Sample List : (8, 2, 3, 0, 7) Expected Output : 20

def cem(mylist):
    x = 0
    for i in mylist:
        x += i
    return x

print(cem((8, 2, 3, 0, 7)))


### 3. - Write a Python function to multiply all the numbers in a list.
#Sample List : (8, 2, 3, -1, 7) Expected Output : -336
import math

def vurma(mylist):
    x = 1
    for i in mylist:
        x *= i
    return x

print(vurma((8, 2, 3, -1, 7)))

### 4. - Write a function called returnDay. 
# This function takes in one parameter ( a number from 1-7) and returns the day of the week 
# ( 1 is Sunday, 2 is Monday etc.). If the number is less than 1 or greater than 7, 
# the function should return None.

def returnday():
    day = int(input('1-7 arasi reqem daxil et: '))
    Day = [ 1, 2, 3, 4, 5, 6, 7 ]
    
    if day in Day:
        if 1 > day < 7:
            print('None')
        if day == (1):
            print('1 is Monday')
        if day == (2):
            print('2 is Tuesday')
        if day == (3):
            print('3 is Wednesday')
        if day == (4):
            print('4 is Thursday')
        if day == (5):
            print('5 is Friday')
        if day == (6):
            print('6 is Saturday')
        if day == (7):
            print('7 is Sunday')
        return
      
returnday()

### 5. - Make a list of five or more usernames, including the name 'admin' . 
# Imagine you are writing code that will print a greeting to each user after they log in to a website.
# Loop through the list, and print a greeting to each user: • If the username is 'admin' , 
# print a special greeting, such as Hello admin, would you like to see a status report? • 
# Otherwise, print a generic greeting, such as Hello Eric, thank you for logging in again.

def users():
    user = input(' istifadeci adinizi daxil edin: ')

    usernames = ['Ali', 'Murad', 'ADMIN',]

    if user in usernames:
        if user == ('ADMIN'):
            print('Hello admin, would you like to see a status report?')
        else:
            print(f'''Hello {user}, thank you for logging in again.''')
        
    else:
        print('siz login olmamisiniz')
    return

users()

### 6. - len() funksiyasini ozunuz yazmaga calishin.

### 7. - funksiya yazin ededlerden ibaret list qebul etsin ve 
# eger listin birinci ve sonuncu elementleri beraberdise return True qaytarsin. 
# Mes: [1,2,3,1] bu halda True qaytaracag


def mylist(list):
    equal = list[0]
    for a in list:
        if a == equal:
            return True
        else:
            return False
            break
          
print(mylist([1, 2, 3, 1]))

