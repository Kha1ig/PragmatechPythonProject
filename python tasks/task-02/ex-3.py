### 3-cu tapşırıq: Proqram run olunanda, istifadəçiyə meyvələr menyusu təqdim olunsun. 
# Userdən menyunuzdakı meyvələrdən birinin adını daxil etməsini tələb edin və ekrana meyvənin qiymətini yazdırın. (İstədiyiniz qiyməti yazdırın). 
# Əgər menyuda olmayan meyvə daxil edilsə, ekrana error mesajı verin.

menu = ['alma', 'armud', 'portagal', 'mandarin', 'kivi', 'nar']
print(menu)
user = input('meyvelerden birini daxil edin: ')

if user in menu:
    print('almanin 1 kq 1.50')
elif user in menu:
    print('armudun 1 kq 1.20')
elif user in menu:
    print('portagal 1 kq 2')
elif user in menu:
    print('mandarin 1 kq 1.70')
else:
    print('daxil etdiyiniz meyve menyuda yoxdur')