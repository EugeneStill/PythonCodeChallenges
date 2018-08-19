def min_max_key_in_dictionary(dict1):
    sorted_list = sorted(list(dict1.keys()))
    return [sorted_list[0], sorted_list[len(sorted_list) - 1]]


print(min_max_key_in_dictionary({2:'a', 7:'b', 1:'c',10:'d',4:'e'})) # [1,10]
print(min_max_key_in_dictionary({1: "Elie", 4:"Matt", 2: "Tim"})) # [1,4]
