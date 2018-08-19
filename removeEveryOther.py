def remove_every_other(l):
    return l[::2]


print(remove_every_other([1,2,3,4,5])) # [1,3,5]
print(remove_every_other([5,1,2,4,1])) # [5,2,1]
print(remove_every_other([1])) # [1]

