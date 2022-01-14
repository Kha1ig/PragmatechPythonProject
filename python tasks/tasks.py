### 1-ci tapşırıq: 3 input daxil edin və daxil edilən ədələrin fərqini tapın.

eded1 = float(input('1-ci ededi daxil edin: '))
eded2 = float(input('2-ci ededi daxil edin: '))
eded3 = float(input('3-cu ededi daxil edin: '))

netice = eded1 - eded2 - eded3 
print(f'netice:{netice}')

### 2-ci tapşırıq: word = 'Python'. Verilen stringin uzerinde azı 5 dənə string method tətbiq edin.

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

### 3-cü tapşırıq: math kitabxanasından istifadə edərək inputdan hələn ədədin kubunu tapın

import math
reqem = pow(float(input('bir reqem daxil edin: ')), 3)

print(reqem)

### 4-cü tapşırıq: inputdan 3 ədəd götürün və o ədələrin kvadratını bir listə əlavə edin.

import math
eded1 = pow(float(input('1-ci ededi daxil edin: ')), 2)
eded2 = pow(float(input('2-ci ededi daxil edin: ')), 2)
eded3 = pow(float(input('3-cu ededi daxil edin: ')), 2)

print(eded1, eded2, eded3)

netice=eded1, eded2, eded3

ededlerinkv=[]
ededlerinkv.extend(netice)

print(ededlerinkv)

### 5-ci tapşırıq: Təsadüfi rəqəmlərdən ibarət olan listin rəqəmlərini kiçikdən böyüyə düzün.

mylist=[ 7, 3, 45, 12, 87, 78, 99, 1, 11 ]

mylist.sort()
print(mylist)

### 6-cı tapşırıq: Bir mesajı dəyişəndə saxlayın və sonra mesajı çapa verin.

text = input('metn daxil edin: ')
print(text)

### 7-ci tapşırıq:  
# ad və soyad dəyişkənləri yaradın və onlara istədiyiniz kiçik hərflərdən ibarət dəyər verin. 
# Sonra tam_ad adlı dəyərdə ad və soyadın ilk hərflərini böyük şəkildə çapa verərək həmin şəxsə Salam verin.
#Nümunə: Salam, Arif Dadaşov! (Ekrana bu yazı çıxsın)

ad = 'ali'
soyad = 'aliyev !'

tam_ad ='Salam,', ad.capitalize(), soyad.capitalize()

x = " ".join(tam_ad)
print( x )

### 8-ci tapşırıq: sep parametrindən istifadə edərək 4 müxtəlif şəhər adını * işarəsi ilə ayırın.

print('Braziliya', 'Turkiye', 'London', sep=" *** ")

### 9-cu tapşırıq: “ Macarıstan” sözünü tərsinə çapa verin.
 
text = 'Macarıstan' [:: -1]
print(text)

### 10-cu tapşırıq: 
# Bir sətir koddan istifadə edərək aşağıdakı yazını göründüyü kimi çapa verin. 
# Languages: Python C JavaScript

print('Languages: Python C Javascript')

### 11-ci tapşırıq: Escape characterlərdən istifadə edərək ekrana bir cümlə çap edin.

text = "We are the so-called \"Vikings\" from the north."
print(text)

### 12-ci tapşırıq: Istenilen bir mətnin tam yarısını çap edin.
# Məsələn: 2 üstü 5 32-dir. (formattingdən istifadə edin)

str = "2 ustu 5 = 32-dir"
new_str = str.replace('=', '')
print(f'''new_str: {new_str}''')

### 13-cü tapşırıq: 
# x = 10, y = 55 “and”-dən istifadə edərək x və y müqayisə edərək boolen dəyərləri çapa verin.

x = int(10)
y = int(55)

if x > y and x > 0:
    print(bool())
if x < y and y > 100:
    print(bool())
if x > y and x < 0:
    print(bool())
    
### 14-cü tapşırıq:
# word = “istədiyiniz sözü yaza bilərsiz” 
# məsələn word = ‘culture’ “Nineteet Eighty-Four does not present "art-as-culture" but "art-as-function"cüməsini bir dəyişkənə mənimsədin və həmin dəyişkəndə saxlayın və word-ə verdiyiniz sözün bu dəyişkəndə olub-olmamasını yoxlayın. 
# Əgər söz varsa, ekranda belə bir nəticə çıxarın;
# “Culture” sözü mətndə var. Əgər yoxdursa, “Not found” çapa verin.

word = 'culture'

text = '''Nineteet Eighty-Four does not present "art-as-culture" but "art-as-function"'''

if 'culture' in text:
    print("'culture' sozu metnde var")
else:
    print("Not found")
    
### 15-ci tapşırıq: 65 ədədinin 22 ədədinə olan qalığı ilə nisbətinin hasilini çapa verin. 

x = 65
y = 22

z = x % y
print('ededin qaligi:', z)
d = x / y
print('ededin bolunmesinden alinan eded:', d)
yekun_netice = z * d
print('cavab:',yekun_netice)

### 16-ci tapşırıq: x-ə istənilən bir ədəd mənimsədin, sonra isə şərt verərək yoxlayın. 
# X 10-dan böyükdürsə və cüt ədədirsə, ekrana “OKAY” yazılsın, 
# əgər yuxarıdakı iki şərtdən biri ödənirsə “NOT OKAY” yazılsın, heç bir şərt ödənməzsə, “BAD” yazılsın 

x = 7

if x > 10 and x % 2 == 0:
    print("OKAY")
if x > 10 or x % 2 == 0:
    print("NOT OKAY")
else:
    print("BAD") 

### 16-ci tapşırıqdan 2-cisi: iki ədəd götürüb dəyişkənlərə mənimsədin. 
# Əgər ədələrin fərqi bir-birlərinə olan nisbətin tam hissəsindən böyükdürsə, 
# ekrana “Greater”, bərabərdirsə, “EQUAL” yox əgər kiçikdirsə, “SMALLER” yazılsın.

x = 10
y = 15
z= x - y
if x-y > x / y:
    print("Greater")
if x-y == x / y:
    print("EQUAL")
if x-y < x / y:
    print("SMALLER")

### 17-ci tapşırıq: String data tipi yaradın və dəyərini 5.567-yə bərabər edin. 
# Sonra bu dəyişkənin dəyərin 10- luqlara qədər yuvarlaqlaşdırın.

number= round(5.567, 10)
print(number)

### 18-ci tapşırıq: my_string = ‘f456.89ts’. 
# my_stringin ədədə bərabər olan hissəsin ilə özündən sonra gələn ən kiçik tam ədədə olan qüvvətini tapın

my_string = 'f456.89ts'
print(my_string.isdigit())


### 19-cu tapşırıq: 1 və 8 arasında random bir ədəd götürsün proqram, 
# sonra isə o ədədin kvadrat kökünü tapın (random kitabxansini research edin).

import random
import math
x = random.randrange(1, 8)
print('random rəqəmi göstər: ', x)
y = math.sqrt(x)
print('ededin kv kökünü göstər', y)

### 20-ci tapşırıq:  0 və 1 arasında olan təsadüfi bir ədədin 1 və 10 arasında olan təsadüfi bir ədələ hasilini tapın.  (random kitabxansini research edin)

import random
x = random.randrange(0, 1)
print(' 1-ci random ededi goster:', x)
y = random.randrange(1, 10)
print(' 2-ci random ededi goster', y)
z = x * y 
print(z)

### 21-ci tapşırıq: x = “5.89” stringinin tam hissəsinin kubunu tapın.

x = "5.89"
z = int(float(x))
y = pow(z, 3)
print(y)

### 22-ci tapşırıq: y = “4.92” stringini integere cast edin.

y = "4.92"
z = int(float(y))
print(z)
