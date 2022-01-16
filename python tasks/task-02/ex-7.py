### Listin en kicik elementini min funksiyasini istifade etmededen tapan alqoritm yazin.

mylist = [5, 50, 2, 22, 10]
x= mylist[0]
for i in mylist[1:]:
    if i < x:
        x = i
        print(x)