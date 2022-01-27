ad = input('adınızı daxil edin: ')
while 3 > len(ad) < 11:
    if  3 > len(ad) < 11:
        ad = input('adınızı 3 - 11 simvol arasi daxil edin: ')
soyad = input('soyadinizi daxil edin: ')
while 5 > len(soyad) < 15:
    if 5 > len(soyad) < 15:
        soyad = input('soyadinizi 5 -15 simvol arasi daxil edin: ')
dogum_ili = int(input('dogum ilinizi daxil edin: '))
while len(dogum_ili) > 4:
    if len(dogum_ili) > 4:
        dogum_ili = int(input('dogum ilini duzgun daxil et: '))
e_mail = input('e-mail daxil edin: ')
while 10 > len(e_mail) < 22:
    if  10 > len(e_mail) < 22:
        e_mail = input('e-mail 10 - 22 simvol arasi daxil edin: ')
        b = '@gmail.com'
        mail = e_mail.__add__(b)
parol = input('parol daxil edin: ')
while 6 > len(parol) <= 13:
    if 6 > len(parol) <= 13:
        parol = input('parol 6 - 13 simvol arasi daxil edin: ')
tesdiq_parolu = input('parolu tesdiqleyin: ')
while tesdiq_parolu != parol:
    if tesdiq_parolu != parol:
        tesdiq_parolu = input('tesdiq parolu duzgun deyil, yendien daxil edin: ')
