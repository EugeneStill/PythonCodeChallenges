def find_the_duplicate(l1):
    l1.sort()
    for i in range(1, len(l1)):
        if l1[i] == l1[i-1]:
            return l1[i]
    return None



print(find_the_duplicate([1,2,1,4,3,12])) # 1
print(find_the_duplicate([6,1,9,5,3,4,9])) # 9
print(find_the_duplicate([2,1,3,4])) # None
