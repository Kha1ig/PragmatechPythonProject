from typing import Iterator


mylist = [27,22,34,44]
mydict = {
    "tural": 27,
    "soltan": 22,
    "zaur": 12,
    "Inci": 23
    }

dictionary = iter(mydict.items())
print(next(dictionary))
print(next(dictionary))
print(next(dictionary))
print(next(dictionary))
mylistim = iter(mylist)
print(next(mylistim))
print(next(mylistim))
print(next(mylistim))
print(next(mylistim))
def list_dic():
    yenilist = []
    if mylistim  == mydict.items:
        yenilist.append(mylistim)
    return yenilist
print(list_dic())

