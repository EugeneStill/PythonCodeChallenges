'''
find_greater_numbers([1,2,3]) # 3
find_greater_numbers([6,1,2,7]) # 4
find_greater_numbers([5,4,3,2,1]) # 0
find_greater_numbers([]) # 0
'''

def find_greater_numbers(list1):
    counter = 0
    for i in range(len(list1) - 1):
        for x in range(len(list1[i:])):
            if list1[i] < list1[x + i]:
                counter += 1
    return counter