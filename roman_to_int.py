def romanToInt(s: str) -> int:
    vals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
        'IV': 4,
        'IX': 9,
        'XL': 40,
        'XC': 90,
        'CD': 400,
        'CM': 900
    }

    end = len(s)
    total = i = 0

    while i < end:
        if i + 1 < end:
            val = '{}{}'.format(s[i], s[i + 1])
            if val in vals:
                total += vals[val]
                i += 2
                continue
        total += vals[s[i]]
        i += 1
    return total

if __name__ == '__main__':
    print(romanToInt('IV'))
    print(romanToInt('MMC'))
    print(romanToInt('XL'))


