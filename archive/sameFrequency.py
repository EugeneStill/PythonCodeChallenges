def same_frequency(n1, n2):
    return sorted(str(n1)) == sorted(str(n2))


print(same_frequency(551122,221515)) # True
print(same_frequency(321142,3212215)) # False
print(same_frequency(1212, 2211)) # True
