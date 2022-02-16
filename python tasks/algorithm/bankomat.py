def atm(a):
    Q = [500, 200, 100, 50, 20, 10,  5, 1]
    x = 0
    for i in range(8):
        q = Q[i]
        x += int(a / q)
        a = int(a % q)
    if a > 0:
        x = -1
        return x
    elif a == 0:
        return x
          
a = int(input('pulu daxil edin: '))

print(atm(a))