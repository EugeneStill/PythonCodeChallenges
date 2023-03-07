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
    def job_scheduling_dp(self, startTime, endTime, profit):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type profit: List[int]
        :rtype: int
        """
        total_jobs = len(startTime)
        jobs = sorted(list(zip(startTime, endTime, profit)))
        print(str(jobs))

        @lru_cache(None)
        def dp(i):
            print("\nIN DP FOR I {}".format(i))
            start, end, profit = 0, 1, 2
            if i == total_jobs:
                print("I IS TOTAL")
                return 0
            # set prelim ans to be job after i
            ans = dp(i + 1)
            print("PRELIM ANS FOR I+1 {}: {}".format(i+1, ans))



            for job in range(i + 1, total_jobs + 1):
                print("LOOPING.  CHECKING JOB {}".format(job))
                if job == total_jobs or jobs[job][start] >= jobs[i][end]:
                    print("GETTING A2: DP({}): {} + JOB I {} PROFIT {}".format(job, dp(job), i, jobs[i][profit]))
                    a2 = dp(job) + jobs[i][profit]
                    print("COMPARING A1 {} TO A2 {}".format(ans, a2))
                    ans = max(ans, a2)
                    break

            return ans

        return dp(0)

    # def job_scheduling_dp_bs(self, start_time, end_time, profit):
    #     n = len(start_time)
    #     jobs = sorted(list(zip(start_time, end_time, profit)))
    #     START, END, PROFIT = 0, 1, 2
    #     start_time = [jobs[i][START] for i in range(n)]
    #
    #     @lru_cache(None)
    #     def dp(i):
    #         if i == n:
    #             print("HIT BASE CASE")
    #             return 0
    #         print("CALLING DP {}".format(i+1))
    #         ans = dp(i + 1)
    #
    #         # instead of looping use binary search (with bisect_left function) to find value of j to use for comparison
    #         j = bisect.bisect_left(start_time, jobs[i][END])
    #         print("GOT J {}".format(j))
    #         print("OLD ANS {} JOB {} PROFIT {}".format(ans, i, jobs[i][PROFIT]))
    #         ans = max(ans, dp(j) + jobs[i][PROFIT])
    #         print("NEW ANS {} DP(j) {}".format(ans, dp(j)))
    #         return ans
    #
    #     return dp(0)

    def job_scheduling_dp_bs(self, start_time, end_time, profit):
        n = len(start_time)
        jobs = sorted(list(zip(start_time, end_time, profit)))
        START, END, PROFIT = 0, 1, 2
        start_time = start_time = [j[START] for j in jobs]
        mem = {}
        def dp(i):

            if i == n:
                print("HIT BASE CASE")
                return 0
            print("CALLING DP {}".format(i+1))
            if i in mem:
                print("GOT I FROM MEM")
                return mem[i]
            print("CALLING DP {}".format(i + 1))
            # since we work backward from base case (which is 0 bc its past end of list of jobs)
            # then we can use our base answer for comparison as dp(i+1), the job after i
            # so when we get to the last job at the end of the list, the answer of i+1 (outside list) will be zero
            ans = mem.get(i+1, dp(i+1))

            # instead of looping use binary search (with bisect_left function) to find value of j to use for comparison
            # j is first job that starts after/at same time as end of job i
            j = bisect.bisect_left(start_time, jobs[i][END])
            dp_j = mem.get(j, dp(j))
            # see if dp_j + profit of job i > current ans
            mem[i] = max(ans, dp_j + jobs[i][PROFIT])
            return mem[i]

        return dp(0)

    def test_job_sched(self):
        start_time = [1, 2, 3, 3]
        end_time = [3, 4, 5, 6]
        profit = [50, 10, 40, 70]
        # self.assertEqual(self.job_scheduling_dp(start_time, end_time, profit), 120)
        self.assertEqual(self.job_scheduling_dp_bs(start_time, end_time, profit), 120)


# LOGGING
# [(1, 3, 50), (2, 4, 10), (3, 5, 40), (3, 6, 70)]
# IN DP FOR I 0
#
# IN DP FOR I 1
#
# IN DP FOR I 2
#
# IN DP FOR I 3
#
# IN DP FOR I 4
# I IS TOTAL
# PRELIM ANS FOR I+1 4: 0
# LOOPING.  CHECKING JOB 4
# GETTING A2: DP(4): 0 + JOB I 3 PROFIT 70
# COMPARING A1 0 TO A2 70
# PRELIM ANS FOR I+1 3: 70
# LOOPING.  CHECKING JOB 3
# LOOPING.  CHECKING JOB 4
# GETTING A2: DP(4): 0 + JOB I 2 PROFIT 40
# COMPARING A1 70 TO A2 40
# PRELIM ANS FOR I+1 2: 70
# LOOPING.  CHECKING JOB 2
# LOOPING.  CHECKING JOB 3
# LOOPING.  CHECKING JOB 4
# GETTING A2: DP(4): 0 + JOB I 1 PROFIT 10
# COMPARING A1 70 TO A2 10
# PRELIM ANS FOR I+1 1: 70
# LOOPING.  CHECKING JOB 1
# LOOPING.  CHECKING JOB 2
# GETTING A2: DP(2): 70 + JOB I 0 PROFIT 50
# COMPARING A1 70 TO A2 120