import unittest
from functools import lru_cache
import bisect
class JobScheduling(unittest.TestCase):
    """
    We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i],
    obtaining a profit of profit[i].

    You're given the startTime, endTime and profit arrays, return the maximum profit you can take such that there are
    no two jobs in the subset with overlapping time range.

    If you choose a job that ends at time X you will be able to start another job that starts at time X.

    Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
    Output: 120
    Explanation: The subset chosen is the first and fourth job.
    Time range [1-3]+[3-6] , we get profit of 120 = 50 + 70.

    https://www.geeksforgeeks.org/bisect-algorithm-functions-in-python/
    https://www.geeksforgeeks.org/python-functools-lru_cache/
    """
    def job_scheduling_dp(self, start_time, end_time, profit):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type profit: List[int]
        :rtype: int
        """
        START, END, PROFIT = 0, 1, 2
        jobs = [(start_time[i], end_time[i], profit[i]) for i in range(len(start_time))]
        jobs.sort(key=lambda x: x[END])
        # Initialize an array to store the maximum profit for each end time
        max_profit = [0] * len(end_time)
        max_profit[0] = jobs[0][PROFIT]

        for curr_job in range(1, len(jobs)):
            older_job = curr_job - 1
            while older_job >= 0 and jobs[older_job][END] > jobs[curr_job][START]:
                older_job -= 1
            max_profit[curr_job] = max(max_profit[curr_job - 1], max_profit[older_job] + jobs[curr_job][PROFIT])
        return max_profit[-1]


    def test_job_sched(self):
        start_time = [1, 2, 3, 3]
        end_time = [3, 4, 5, 6]
        profit = [50, 10, 40, 70]
        self.assertEqual(self.job_scheduling_dp(start_time, end_time, profit), 120)


# LOGGING
# I 1 J -1 MP [50, 50, 0, 0]
# I 2 J 0 MP [50, 50, 90, 0]
# I 3 J 0 MP [50, 50, 90, 120]