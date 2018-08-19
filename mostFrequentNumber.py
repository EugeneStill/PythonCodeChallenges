'''
mode([2,4,1,2,3,3,4,4,5,4,4,6,4,6,7,4]) # 4
'''

# define mode below:
def mode(list1):
    high_count = 0
    mode_number = 0
    for i in range(10):
        if list1.count(i) > high_count:
            mode_number = i
            high_count = list1.count(i)
    return mode_number