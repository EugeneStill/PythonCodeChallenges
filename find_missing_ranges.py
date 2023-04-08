class FindMissingRanges(object):
    def find_missing_ranges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        result = []

        # Helper function to append a missing range to the result list
        def add_range(start, end):
            if start == end:
                result.append(str(start))
            else:
                result.append(str(start) + "->" + str(end))

        # Check for missing range before the first number
        if nums and nums[0] > lower:
            add_range(lower, nums[0] - 1)

        # Check for missing ranges between numbers
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] > 1:
                add_range(nums[i - 1] + 1, nums[i] - 1)

        # Check for missing range after the last number
        if nums and nums[-1] < upper:
            add_range(nums[-1] + 1, upper)

        return result
