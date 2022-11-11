def Merge(dict1, dict2):
    m = {**dict1, **dict2}
    return m
     
dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}
dict3 = Merge(dict1, dict2)
print(dict3)
