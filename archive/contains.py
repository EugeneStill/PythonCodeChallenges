'''
pass collection, value and optional starting index
collection can be dict, list or string
return whether value is found (using starting index as the eligible starting point if passed
'''
def includes(collection, value, start=0):
    if type(collection) == dict:
        return value in collection.values()
    return value in collection[start:]



print(includes([1, 2, 3], 1)) # True
print(includes([1, 2, 3], 1, 2)) # False
print(includes({ 'a': 1, 'b': 2 }, 1)) # True
print(includes({ 'a': 1, 'b': 2 }, 'a')) # False
print(includes('abcd', 'b')) # True
print(includes('abcd', 'e')) # False
