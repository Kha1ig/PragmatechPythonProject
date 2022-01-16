### Qeydiyyat formu düzəldin. İstifadəçi adını daxil etsin. A
# dın uzunlu 3-dən kiçik 11-dən böyük ola bilməz.
# Əgər adını düzgün daxil edərsə, soyadının daxil etməsini istəyin. 
# Soyad 5 hərfdən kiçik, 15 hərfdən uzun olmasın. 
# Əgər soyad düzgün daxil edilsə, Daha sonra doğulduğu ili daxil etsin. 
# Doğum ilinin uzunluğu 4 simvoldan ibarət olmalıdır. 
# Sonra email daxil etməsini tələb edin. 
# Emailin uzunluğu 10 hərifdən qısa 22 hərfdən uzzun olmasın, 
# tərkibində @gmail.com olsun və bu hissə daxil etdiyi emailin sonunda olsun. 
# Ardınca parol axil etsin. Parol 6-13 simvol aralığında olmalıdır. 
# Sonra parolu təsdiqləməyini tələb edin. 
# Təsdiqlədiyi parol birinci yazdığı parol ilə eyni olmalıdır. 
# Bütün bunlar düzgün daxil edilərsə, 
# Qeydiyyat tamamlandı mesajı verilsin və istifadəçidən qeydiyyatın detallarına baxmaq istəyib-istəməməsi soruşulsun. 
# Əgər hə desə, aşağıdakı görüntü çapa verilsin: 
# (Qeyd: Yuxarıda sizin verdiyiniz şərtlərə uyğun istifadəçi input daxil etmsəsə, hər verdiyibiz şərtə uyğun error tipli mesaj verin. Məsələn doğum ilini 5 simvoldan ibarət daxil etsə, mesaj verilsin ki 4 simvol daxil edin. Yəni hər şərti müvafiq mesajlar ilə userə izah edin. ============================================= Ad: Murad Soyad: Əliyev Yaş: 22 Email: muradaliyev1996@gmail.com Parol: 123456789 
# ============================================= 
# Əgər yox desə, Murad Əliyev, Uğurlar! Yazılsın.

ad = input('adınızı daxil edin: ')
if  3 < len(ad) < 11:
    soyad = input('soyadinizi daxil edin: ')
    if 5 < len(soyad) < 15:
        dogum_ili = input('dogum ilinizi daxil edin: ')
        if len(dogum_ili) == 4:
            if len(dogum_ili) > 5:
                    dogum_ili = input('dogum ilini duzgun daxil et: ')
            e_mail = input('e-mail daxil edin: ')
            if  10 < len(e_mail) < 22:
                b = '@gmail.com'
                mail = e_mail.__add__(b)
                parol = input('parol daxil edin: ')
                if 6 < len(parol) <= 13:
                    tesdiq_parolu = input('parolu tesdiqleyin: ')
                    while tesdiq_parolu != parol:
                        if tesdiq_parolu != parol:
                            tesdiq_parolu = input('tesdiq parolu duzgun deyil: ')

cavab = input('Qeydiyyat tamamlandi ve qeydiyyatın detallarına baxmaq istəyirsinizmi  hE ya yox: ')
print(cavab)

if cavab == ('he'):
    print(f'''ad: {ad}, soyad: {soyad}, dogum_ili: {dogum_ili}, mail: {mail}, parol: {parol}''' )
else:
    print('___ugurlar!___')

            
            
    