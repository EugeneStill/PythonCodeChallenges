'''
reverse_vowels("Hello!") # "Holle!"
reverse_vowels("Tomatoes") # "Temotaos"
reverse_vowels("Reverse Vowels In A String") # "RivArsI Vewols en e Streng"
reverse_vowels("aeiou") # "uoiea"
reverse_vowels("why try, shy fly?") # "why try, shy fly?"
'''


def reverse_vowels(string):
    vowels = [char for char in string if char.lower() in "aeiou"]
    new_string = list(string)
    for i in range(len(string)):
        if string[i].lower() in "aeiou":
            new_string[i] = vowels.pop()
    return (''.join(new_string))
