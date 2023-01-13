


def twoSum(nums, target):
    seen = {}
    for count, n in enumerate(nums):
        print("{} {}".format(count, n))
        if target - n in seen:
            return [count, seen[target - n]]
        else:
            seen[n] = count

if __name__ == '__main__':
    print(twoSum([3,2,4], 6))


