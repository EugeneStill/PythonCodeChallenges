def range_in_list(l, s=0, e=None):
    e = e or len(l) - 1
    return sum(l[s:e+1])


print(range_in_list([1,2,3,4],0,2)) #  6
print(range_in_list([1,2,3,4],0,3)) # 10
print(range_in_list([1,2,3,4],1)) #  9
print(range_in_list([1,2,3,4])) # 10
print(range_in_list([1,2,3,4],0,100)) # 10
print(range_in_list([],0,1)) # 0
