### argument sayını bilmiriksə nece tapmaq olar

def func(*names):
    print('ad çap olundu', names)

func('ben', 'jhon' )

### Write a Python function to check whether a number is perfect or not. Go to the editor
# According to Wikipedia : In number theory, a perfect number is a positive integer that is equal to the sum of its proper positive divisors, 
# that is, the sum of its positive divisors excluding the number itself (also known as its aliquot sum). 
# Equivalently, a perfect number is a number that is half the sum of all of its positive divisors (including itself).
# Example : The first perfect number is 6, because 1, 2, and 3 are its proper positive divisors, 
# and 1 + 2 + 3 = 6. Equivalently, the number 6 is equal to half the sum of all its positive divisors: 
# ( 1 + 2 + 3 + 6 ) / 2 = 6. The next perfect number is 28 = 1 + 2 + 4 + 7 + 14. 
# This is followed by the perfect numbers 496 and 8128.

def numberfind(n):
    x = 0
    newlist = []
    for i in range(1, n):
        if (n % i) == 0:
            x += i
            newlist.append(x)
            print(newlist)
    return x == n
number = int(input('number add: '))
print(numberfind(number))

### Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetica

str_txt = input('metn daxil edin: ')
x = str_txt.split('-')
x.sort()
print('-'.join(x))