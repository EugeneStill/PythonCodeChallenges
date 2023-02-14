import unittest
from heapq import heappush, heappop
from collections import Counter
class LeastInterval(unittest.TestCase):
    """
    Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a
    different task. Tasks could be done in any order. Each task is done in one unit of time.
    For each unit of time, the CPU could complete either one task or just be idle.

    However, there is a non-negative integer n that represents the cooldown period between two same tasks
    (the same letter in the array), that is that there must be at least n units of time between any two same tasks.

    Return the least number of units of time that the CPU will take to finish all the given tasks.
    """
    def least_interval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        time_units, pq = 0, []
        for task, task_count in Counter(tasks).items():
            heappush(pq, (-1*task_count, task))
        print("\n{}".format(str(pq)))
        while pq:
            completed_task_count, temp = 0, []
            # for each while loop complete n time units
            while completed_task_count <= n:
                print("\nADDING TIME UNIT FOR {} COMPLETED TASKS".format(completed_task_count))
                time_units += 1
                if pq:
                    # heap pop will pop the smallest number of tasks
                    # since we're using negative numbers that is the task with highest count remaining
                    temp_count, temp_tsk = heappop(pq)
                    print("POPPED TASK: {} COUNT: {}".format(temp_tsk, temp_count))
                    if temp_count != -1:
                        print("ADDED TASK: {} COUNT: {} TO TEMP".format(temp_tsk, temp_count))
                        temp.append((temp_count + 1, temp_tsk))
                if not pq and not temp:
                    print("NO PQ & NO TEMP")
                    break
                # completed task could be an actual task or an idle unit of time
                elif not temp:
                    print("NO TEMP. COMPLETED 1 TASK")
                    completed_task_count += 1
                else:
                    print("NO PQ, COMPLETED 1 TASK")
                    completed_task_count += 1
            # after each while loop, push any temp items to pq
            for item in temp:
                print("PUSHING {} TO PQ".format(str(item)))
                heappush(pq, item)
        return time_units

    def test_task_scheduler(self):
        self.least_interval(["A","A","A","A","A","A","B","C","D","E","F","G"], 2)

# LOGGING
# [(-6, 'A'), (-1, 'B'), (-1, 'C'), (-1, 'D'), (-1, 'E'), (-1, 'F'), (-1, 'G')]
#
# ADDING TIME UNIT FOR 0 COMPLETED TASKS
# POPPED TASK: A COUNT: -6
# ADDED TASK: A COUNT: -6 TO TEMP
# NO PQ, COMPLETED 1 TASK
#
# ADDING TIME UNIT FOR 1 COMPLETED TASKS
# POPPED TASK: B COUNT: -1
# NO PQ, COMPLETED 1 TASK
#
# ADDING TIME UNIT FOR 2 COMPLETED TASKS
# POPPED TASK: C COUNT: -1
# NO PQ, COMPLETED 1 TASK
# PUSHING (-5, 'A') TO PQ
#
# ADDING TIME UNIT FOR 0 COMPLETED TASKS
# POPPED TASK: A COUNT: -5
# ADDED TASK: A COUNT: -5 TO TEMP
# NO PQ, COMPLETED 1 TASK
#
# ADDING TIME UNIT FOR 1 COMPLETED TASKS
# POPPED TASK: D COUNT: -1
# NO PQ, COMPLETED 1 TASK
#
# ADDING TIME UNIT FOR 2 COMPLETED TASKS
# POPPED TASK: E COUNT: -1
# NO PQ, COMPLETED 1 TASK
# PUSHING (-4, 'A') TO PQ
#
# ADDING TIME UNIT FOR 0 COMPLETED TASKS
# POPPED TASK: A COUNT: -4
# ADDED TASK: A COUNT: -4 TO TEMP
# NO PQ, COMPLETED 1 TASK
#
# ADDING TIME UNIT FOR 1 COMPLETED TASKS
# POPPED TASK: F COUNT: -1
# NO PQ, COMPLETED 1 TASK
#
# ADDING TIME UNIT FOR 2 COMPLETED TASKS
# POPPED TASK: G COUNT: -1
# NO PQ, COMPLETED 1 TASK
# PUSHING (-3, 'A') TO PQ
#
# ADDING TIME UNIT FOR 0 COMPLETED TASKS
# POPPED TASK: A COUNT: -3
# ADDED TASK: A COUNT: -3 TO TEMP
# NO PQ, COMPLETED 1 TASK
#
# ADDING TIME UNIT FOR 1 COMPLETED TASKS
# NO PQ, COMPLETED 1 TASK
#
# ADDING TIME UNIT FOR 2 COMPLETED TASKS
# NO PQ, COMPLETED 1 TASK
# PUSHING (-2, 'A') TO PQ
#
# ADDING TIME UNIT FOR 0 COMPLETED TASKS
# POPPED TASK: A COUNT: -2
# ADDED TASK: A COUNT: -2 TO TEMP
# NO PQ, COMPLETED 1 TASK
#
# ADDING TIME UNIT FOR 1 COMPLETED TASKS
# NO PQ, COMPLETED 1 TASK
#
# ADDING TIME UNIT FOR 2 COMPLETED TASKS
# NO PQ, COMPLETED 1 TASK
# PUSHING (-1, 'A') TO PQ
#
# ADDING TIME UNIT FOR 0 COMPLETED TASKS
# POPPED TASK: A COUNT: -1
# NO PQ & NO TEMP