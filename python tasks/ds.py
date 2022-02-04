
mylist = [27,22,34,44]
dic = {
    "tural": 27,
    "soltan": 22,
    "zaur": 12,
    "Inci": 23
    }

d = dic
def clear_dict(d):
    if dic is None:
        return None
    elif isinstance(dic, mylist):
        return mylist(filter(lambda x: x is not None, map(clear_dict, d)))
    elif not isinstance(dic, dict):
        return dic
    else:
        r = dict(
                filter(lambda x: x[1] is not None,
                    map(lambda x: (x[0], clear_dict(x[1])),
                        dic.items())))
        if not bool(r):
            return None
        return r
clear_dict(dic)