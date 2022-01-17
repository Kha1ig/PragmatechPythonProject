### 1-ci tapşırıq:
# Kvadrat yaratmaq olarsa daxil edilən 4 ədəddən, 
# ekrana kvadratın sahəsini, olmazsa, həmin ədədlərin cəmini verin.

reqem1 = int(input('1-ci reqemi daxil edin: '))
reqem2= int(input('2-ci reqemi daxil edin: '))
reqem3 = int(input('3-ci reqemi daxil edin: '))
reqem4 = int(input('4-ci reqemi daxil edin: '))

if reqem1==reqem2 and reqem3 == reqem4 and reqem2 == reqem3 :
    print(reqem1**2)
else:
    print(reqem1+reqem2+reqem3+reqem4)