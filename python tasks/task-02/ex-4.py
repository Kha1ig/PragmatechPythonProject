### Qeydiyyat formu düzəldin. İstifadəçi adını daxil etsin. 
# Adın uzunlu 3-dən kiçik 11-dən böyük ola bilməz.
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
import re 
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'  

def reseption():
    ad = input('adınızı daxil edin: ')
    while 3 > len(ad) < 11:
        if  3 > len(ad) < 11:
            ad = input('adınızı 3 - 11 simvol arasi daxil edin: ')
    soyad = input('soyadinizi daxil edin: ')
    while 5 > len(soyad) < 15:
        if 5 > len(soyad) < 15:
            soyad = input('soyadinizi 5 -15 simvol arasi daxil edin: ')
    dogum_ili = input('dogum ilinizi daxil edin: ')
    while (len(dogum_ili)) > 4:
        if len(dogum_ili) > 4:
            dogum_ili = input('dogum ilini duzgun daxil et: ')
    e_mail = input('e-mail daxil edin: ')
    while 10 > len(e_mail) < 22 or e_mail[len(e_mail)-len('@gmail.com')::] != '@gmail.com':
        if(re.search(regex,e_mail)):   
            print("Valid Email")   
        else:   
            print("Invalid Email")
        if  10 > len(e_mail) < 22:
            e_mail = input('e-mail 10 - 22 simvol arasi daxil edin: ')
    parol = input('parol daxil edin: ')
    while 6 > len(parol) <= 13:
        if 6 > len(parol) <= 13:
            parol = input('parol 6 - 13 simvol arasi daxil edin: ')
    tesdiq_parolu = input('parolu tesdiqleyin: ')
    while tesdiq_parolu != parol:
        if tesdiq_parolu != parol:
            tesdiq_parolu = input('tesdiq parolu duzgun deyil, yendien daxil edin: ')

    cavab = input('Qeydiyyat tamamlandi ve qeydiyyatın detallarına baxmaq istəyirsinizmi  he ya yox: ')
    print(cavab)
    dic ={
        'ad':ad,
        'soyad':soyad,
        'dogum_ili': dogum_ili,
        'e-mail': e_mail,
        'parol': parol
        
    }

    if cavab == ('he'):
        for k, v in dic.items():
            print (k, ':', v)
    else:
        print(dic.get('ad'),dic.get('soyad'), '_ugurlar!_')

    cavab2 =input('yeni qeydiyyat baslasinmi he ya yox: ')
    if cavab2 == ('he'):
        reseption() 
    else:
        
        return dic
reseption()


            
            