


def twoSum(nums, target):
    seen = {}
    for i, n in enumerate(nums):
        if target - n in seen:
            return [i, seen[target - n]]
        else:
            seen[n] = i

if __name__ == '__main__':
    print(twoSum([3,2,4], 6))


