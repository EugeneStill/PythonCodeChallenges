import unittest

class DailyTemperatures(unittest.TestCase):

    def daily_temperatures(self, T):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        #initialize the result array with all '0's considering when there is no bigger temperature
        #temp in variable names refer to 'temperature', not 'temporary'
        ans = [0]*len(T)
        stack = []

        for temp_index,current_temp in enumerate(T):
            #check if list current temp > last appended stack val.  Pop all the elements < current temp
            while stack and stack[-1][1] < current_temp:
                stack_index,stack_temp = stack.pop()
                # update ans with difference between current temp_index and stack_index (last time we had lesser temp)
                ans[stack_index] = temp_index - stack_index
            stack.append([temp_index,current_temp])

        return ans

    def test_dt(self):
        input1 = [73,74,75,71,69,72,76,73]
        expected1 = [1,1,4,2,1,1,0,0]
        input2 = [30,40,50,60]
        expected2 = [1,1,1,0]
        input3 = [30,60,90]
        expected3 = [1,1,0]
        self.assertEqual(self.daily_temperatures(input1), expected1)
        self.assertEqual(self.daily_temperatures(input2), expected2)
        self.assertEqual(self.daily_temperatures(input3), expected3)


# LOGGING
# ****** CHECKING TEMP: 73 I: 0
# STACK IS [[0, 73]]
# ANS IS [0, 0, 0, 0, 0, 0, 0, 0]
#
# ****** CHECKING TEMP: 74 I: 1
# POPPED 73
# STACK IS [[1, 74]]
# ANS IS [1, 0, 0, 0, 0, 0, 0, 0]
#
# ****** CHECKING TEMP: 75 I: 2
# POPPED 74
# STACK IS [[2, 75]]
# ANS IS [1, 1, 0, 0, 0, 0, 0, 0]
#
# ****** CHECKING TEMP: 71 I: 3
# STACK IS [[2, 75], [3, 71]]
# ANS IS [1, 1, 0, 0, 0, 0, 0, 0]
#
# ****** CHECKING TEMP: 69 I: 4
# STACK IS [[2, 75], [3, 71], [4, 69]]
# ANS IS [1, 1, 0, 0, 0, 0, 0, 0]
#
# ****** CHECKING TEMP: 72 I: 5
# POPPED 69
# POPPED 71
# STACK IS [[2, 75], [5, 72]]
# ANS IS [1, 1, 0, 2, 1, 0, 0, 0]
#
# ****** CHECKING TEMP: 76 I: 6
# POPPED 72
# POPPED 75
# STACK IS [[6, 76]]
# ANS IS [1, 1, 4, 2, 1, 1, 0, 0]
#
# ****** CHECKING TEMP: 73 I: 7
# STACK IS [[6, 76], [7, 73]]
# ANS IS [1, 1, 4, 2, 1, 1, 0, 0]
# PASSED

