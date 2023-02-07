import unittest


class ProductExceptSelf(unittest.TestCase):
    """
    Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements
    of nums except nums[i].

    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

    You must write an algorithm that runs in O(n) time and without using the division operation.
    """
    def product_except_self(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        print("\n")
        acc = 1
        # work forward in list & accumulate product of previous numbers in the res list thus excluding current num
        for n in nums:
            res.append(acc)
            acc *= n
            print(str(res))
        acc = 1
        print("backtrack")
        # now work backwards, and update product in the opposite direction while also excluding current num
        for i in reversed(range(len(nums))):
            res[i] *= acc
            print(str(res))
            acc *= nums[i]
        return res

    def test_pes(self):
        self.assertEqual(self.product_except_self([1,2,3,4]), [24,12,8,6])