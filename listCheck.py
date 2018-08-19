


def list_check(l):
    return all(type(item) == list for item in l)

print(list_check([[],[1],[2,3], (1,2)])) # False
print(list_check([1, True, [],[1],[2,3]])) # False
print(list_check([[],[1],[2,3]])) # True