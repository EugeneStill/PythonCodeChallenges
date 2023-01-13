def two_list_dictionary(a, b):
    return {**{}.fromkeys(a, None), **dict(zip(a,b))}


print(two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3])) # {'a': 1, 'b': 2, 'c': 3, 'd': None}
print(two_list_dictionary(['a', 'b', 'c']  , [1, 2, 3, 4])) # {'a': 1, 'b': 2, 'c': 3}
print(two_list_dictionary(['x', 'y', 'z']  , [1,2])) # {'x': 1, 'y': 2, 'z': None}

'''
create new dict with all elements from list a as keys
overlay the new dict with a zip of list a & b
the keys (elements from list a) won't change and the values (all elements from list b will only overlay the "None" 
values until the last element of list b is reachec
values until the last element of list b is reachec
'''