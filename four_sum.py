import unittest

class FourSum(unittest.TestCase):

    def four_sum(self, nums, target):
        nums = sorted(nums)
        if not nums or nums[0] * 4 > target or nums[-1] * 4 < target:
            return []
        results = {}

        n = len(nums)
        for a in range(n - 3):
            for b in range(a + 1, n - 2):
                trgt = target - nums[a] - nums[b]
                c, d = b + 1, n - 1
                while c < d:
                    print("checking: {} {} {} {}".format(a, b, c, d))
                    sum_val = nums[c] + nums[d]
                    if sum_val == trgt:
                        soln = [nums[a], nums[b], nums[c], nums[d]]
                        results[str(soln)] = soln
                        c += 1
                        d -= 1
                    elif sum_val < trgt:
                        c += 1
                    else:
                        d -= 1

        return list(results.values())

    def test_fs(self):
        self.assertEqual(self.four_sum([1,0,-1,0,-2,2], 0), [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]])



