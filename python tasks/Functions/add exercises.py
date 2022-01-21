### argument sayını bilmiriksə nece tapmaq olar

def func(*names):
    print('ad çap olundu', names)

func('ben', 'jhon' )

###

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