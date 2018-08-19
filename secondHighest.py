'''
Return index of second highest (penultimate) integer from a list of integers
'''


def find_pni(list1):
    pni = -1
    if type(list1) != list:
        return pni
    if len(list1) < 2:
        return pni
    if any(type(i) != int for i in list1):
        return pni
    hi = max(sorted(list1))
    pn_value = min(sorted(list1))
    for i in range(len(list1)):
        if list1[i] != hi and list1[i] >= pn_value:
            pni = i
            pn_value = list1[i]
    return pni


print(find_pni({'a': 1, 'b': 2}))  # -1
print(find_pni([1]))  # -1
print(find_pni(['a', 5, 5]))  # -1
print(find_pni([1, 2]))  # 0
print(find_pni([2, 1]))  # 1
print(find_pni([2, 1, 3]))  # 0
print(find_pni([1, 2, 3]))  # 1
print(find_pni([1, 5, 2]))  # 2
print(find_pni([1, 5, 5, 2]))  # 3
print(find_pni([5, 5, 5]))  # -1


