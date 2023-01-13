def titleize(s):
    return ' '.join(word[0].upper() + word[1:] for word in s.split())


print(titleize('this is awesome')) # "This Is Awesome"
print(titleize('oNLy cAPITALIZe fIRSt'))# "ONLy CAPITALIZe FIRSt"
