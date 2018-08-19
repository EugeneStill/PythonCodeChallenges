def isPalindrome(s):
    if s == s[::-1]:
        return True
    return False

print(isPalindrome("Otto")) #False
print(isPalindrome("HuH")) #True
