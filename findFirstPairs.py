#RETURN FIRST PAIR OF NUMBERS FROM LIST THAT ADD UP TO n

def sum_pairs(l, n):
    already_visited = set()
    for i in l:
        difference = n - i
        if difference in already_visited:
            return [difference, i]
        already_visited.add(i)
    return []


print(sum_pairs([4,2,10,5,1], 6))# [4,2]
print(sum_pairs([11,20,4,2,1,5], 100)) # []

