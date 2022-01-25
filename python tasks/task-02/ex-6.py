### Listin en boyuk elementini max funksiyasini istifade etmededen tapan alqoritm yazin.

mylist = [5, 50, 2, 22, 100,448]
x= mylist[0]
for i in mylist:
    if i > x:
        x = i
print(x)