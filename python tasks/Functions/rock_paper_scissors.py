import random
oyuncu = input('ad axil edin: ')
mylist = 'das', 'qayci', 'kagiz'

def randomlist():
    a = input('kagiz, qayci, das: ')
    
    x = random.choice(mylist)
    print(x)
    if a == x:
        print(f'''{oyuncu} cavab duzdur''')
    else:
        print('bextini bir daha sina')
    
    yenioyun = input('yeniden oynamaq isteyirsenmi y/n: ')
    if yenioyun == ('y'):
        print(randomlist())
    else:
        exit
    return oyuncu 
    
print(randomlist())