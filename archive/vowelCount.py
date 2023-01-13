def vowel_count(s):
    s = s.lower()
    return {v:s.count(v) for v in 'aeiou' if v in s}

print(vowel_count('awesome')) # {'a': 1, 'e': 2, 'o': 1}
print(vowel_count('Elie')) # {'e': 2, 'i': 1}
print(vowel_count('Colt')) # {'o': 1}
