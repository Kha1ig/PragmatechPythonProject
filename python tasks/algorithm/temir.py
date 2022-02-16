sifaris = int(input('sifarisin sayi: '))

def sifaris_sayi():
    area = []
    for i in range(sifaris):
        L = int(input('uzunlugu daxil edin: '))
        w = int(input('eni daxil edin: '))
        H = int(input('hundurluyu daxil edin: '))

        S = (2 *L*H + 2*w*H) - 1
        area.append(S)
    return area

def boya(mylist):
    for a in mylist:
        banka = 16
        z = a / banka
        
        print(round(z))
boya(sifaris_sayi())