def isPalindrome(x: int) -> bool:
    # string comparison
    # return str(x)[::-1] == str(x)

    #
    if x < 0:
        return False
    n = x
    n1 = 0
    while (n > 0):
        n1 = (n1 * 10) + (n % 10)
        n = n // 10
    return n1 == x

if __name__ == '__main__':
    print(isPalindrome(-121))
    print(isPalindrome(0))
    print(isPalindrome(1001))


