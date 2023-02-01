class SmallestDistancePair(object):
    def smallest_distance_pair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def enough(distance):  # two pointers
            print("D: {}".format(distance))
            count, i, j = 0, 0, 0
            while i < n or j < n:
                print("NUMS J {} NUMS I {}".format(nums[j], nums[i]))
                while j < n and nums[j] - nums[i] <= distance:
                    j += 1
                count += j - i - 1
                i += 1
            return count >= k

        nums.sort()
        n = len(nums)
        print(n)
        left, right = 0, nums[-1] - nums[0]
        while left < right:
            mid = (right + left) // 2
            if not enough(mid):
                left = mid + 1
            else:
                right = mid
        return left

    def test_sdp(self):
        self.smallest_distance_pair([1,6,1,8,9,10,12,18,7], 5)