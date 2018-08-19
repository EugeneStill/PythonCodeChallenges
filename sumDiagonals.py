def sum_diagonals(l1):
    total = 0
    for i in range(len(l1)):
        if len(l1) % 2 == 1 and i == len(l1) // 2:
            total += l1[i][i] * 2
        else:
            total += l1[i][i] + l1[i][-1 - i]
    print(total)
    return total


list1 = [
  [ 1, 2 ],
  [ 3, 4 ]
]
sum_diagonals(list1) # 10

list2 = [
  [ 1, 2, 3 ],
  [ 4, 5, 6 ],
  [ 7, 8, 9 ]
]
sum_diagonals(list2) # 30

list3 = [
  [ 4, 1, 0 ],
  [ -1, -1, 0],
  [ 0, 0, 9]
]
sum_diagonals(list3) # 11

list4 = [
  [ 1, 2, 3, 4 ],
  [ 5, 6, 7, 8 ],
  [ 9, 10, 11, 12 ],
 [ 13, 14, 15, 16 ]
]
sum_diagonals(list4) # 68
