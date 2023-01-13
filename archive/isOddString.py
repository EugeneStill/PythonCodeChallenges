'''
is_odd_string('a') # True
is_odd_string('aaaa') # False
is_odd_string('amazing') # True
is_odd_string('veryfun') # True
is_odd_string('veryfunny') # False
'''
import string

def is_odd_string(string):
    # letters = string.ascii_lowercase
    letters = 'abcdefghijklmnopqrstuvwxyz'
    alpha = {letters[x]:x+1 for x in range(26)}
    total = 0
    for char in string:
        total += int(alpha.get(char))
    if total % 2 == 0:
        return False
    return True