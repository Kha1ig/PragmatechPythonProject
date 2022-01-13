### 1-ci tapşırıq:

eded1 = float(input('1-ci ededi daxil edin: '))
eded2 = float(input('2-ci ededi daxil edin: '))
eded3 = float(input('3-cu ededi daxil edin: '))

netice = eded1 - eded2 - eded3 
print(f'netice:{netice}')

### 2-ci tapşırıq:

word = 'Python'

w = word.center(20, "_")
a = word.encode()
x = word.swapcase()
z = word.isidentifier()

print(w)
print(a)
print(x)
print(z)
print(word.isascii())
print(word.isdecimal())
print(word.isdigit())

### 3-cü tapşırıq:

import math
reqem = pow(float(input('bir reqem daxil edin: ')), 3)

print(reqem)

### 4-cü tapşırıq:

import math
eded1 = pow(float(input('1-ci ededi daxil edin: ')), 2)
eded2 = pow(float(input('2-ci ededi daxil edin: ')), 2)
eded3 = pow(float(input('3-cu ededi daxil edin: ')), 2)

print(eded1, eded2, eded3)

netice=eded1, eded2, eded3

ededlerinkv=[]
ededlerinkv.extend(netice)

print(ededlerinkv)

### 5-ci tapşırıq:

mylist=[ 7, 3, 45, 12, 87, 78, 99, 1, 11 ]

mylist.sort()
print(mylist)

### 6-cı tapşırıq:

### 7-ci tapşırıq:

ad = 'ali'
soyad = 'aliyev !'

tam_ad ='Salam,', ad.capitalize(), soyad.capitalize()

x = " ".join(tam_ad)
print( x )

### 8-ci tapşırıq:

print('Braziliya', 'Turkiye', 'London', sep=" *** ")

### 9-cu tapşırıq:
 
text = 'Macarıstan' [:: -1]
print(text)

### 10-cu tapşırıq:
print('Languages: Python C Javascript')

### 11-ci tapşırıq:

text = "We are the so-called \"Vikings\" from the north."
print(text)

### 12-ci tapşırıq:

str = "2 ustu 5 = 32-dir"
new_str = str.replace('=', '')
print(new_str)

### 13-cü tapşırıq:

x = int(10)
y = int(55)

if x and y > 0:
    print(bool())
    
### 14-cü tapşırıq:

word = 'culture'

text = '''Nineteet Eighty-Four does not present "art-as-culture" but "art-as-function"'''

if 'culture' in text:
    print("'culture' sozu metnde var")
else:
    print("Not found")
    
### 15-ci tapşırıq:

x = 65
y = 22

z = x % y
print('ededin qaligi:', z)
d = x / y
print('ededin bolunmesinden alinan eded:', d)
yekun_netice = z * d
print('cavab:',yekun_netice)

### 16-ci tapşırıq:

x = 7

if x > 10 and x % 2 == 0:
    print("OKAY")
if x > 10 or x % 2 == 0:
    print("NOT OKAY")
else:
    print("BAD") 

### 16-ci tapşırıqdan 2-cisi:

x = 10
y = 15
z= x - y
if x-y > x / y:
    print("Greater")
if x-y == x / y:
    print("EQUAL")
if x-y < x / y:
    print("SMALLER")

### 17-ci tapşırıq:

number= round(5.567, 10)
print(number)

### 18-ci tapşırıq:

my_string = 'f456.89ts'
str_list = my_string.split()
print(str_list)


### 19-cu tapşırıq:

import random
import math
x = random.randrange(1, 8)
print('random rəqəmi göstər: ',x)
y = math.sqrt(x)
print('ededin kv kökünü göstər',y)

### 20-ci tapşırıq:

import random
x = random.randrange(0, 1)
print(' 1-ci random ededi goster:', x)
y = random.randrange(1, 10)
print(' 2-ci random ededi goster', y)
z = x * y 
print(z)

### 21-ci tapşırıq:

x = "5.89"
z = int(float(x))
y = pow(z, 3)
print(y)

### 22-ci tapşırıq:

x = "4.92"
z = int(float(x))
print(z)
