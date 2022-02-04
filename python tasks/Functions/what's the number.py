import random

print('''                                                ___Nömrəni tap oynuna xoş gəlmisiniz___
                                                    _____Hadi oyun başlasın_____''')
oyuncu1 = input('zəhmət olmasa 1-ci oyunçu adını daxil edin:')
oyuncu2 = input('zəhmət olmasa 2-ci oyunçu adını daxil edin: ')

y = 1
while y < 5:
    y += 1    
    a = int(input(f'''{oyuncu1} 1-10 arası rəqəm daxil edin: '''))
    b = int(input(f'''{oyuncu2} 1-10 arası rəqəm daxil edin: '''))
    def randomnumber():
        x = random.randint(0,10)
        print('random seçilən rəqəm', x)
        
        if a == x and b != x:
            print(f'''                                                   ___{oyuncu1}-in cavabı dogrudur___''')
            print(f'''                                                   {oyuncu2} cavabı bilmədi''')
            print(f'''                                               Hadi {oyuncu2} məyus olma oyun qabaqdadır''')
        if a != x and b == x:
            print(f'''                                           ___{oyuncu1} cavabı bilmədi ancaq oyun qabaqdadır''')
            print(f'''                                               ___{oyuncu2} adlı oyuncu gözəl oyun aparır___''')
        if a == x and b == x:
            print(f'''                             _-_ Afərin sizə {oyuncu1} ve {oyuncu2} görünür kompüterlə eyni fikiri bölüşürsünüz _-_''')
        if a != x and b !=x:
            print('                             hec bir oyuncu rəqəmi tapa bilmədi novbəti dəfə şansınızı yoxlayın bu bir oyun zövq alın')
            print(f'''                                            Hadi {oyuncu1} ve {oyuncu2} oyun 5 raunddan ibarətdir ''')
        return oyuncu1 (5 - y)
    randomnumber()