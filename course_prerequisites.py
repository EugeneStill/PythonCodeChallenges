import unittest
import collections

class CoursePrereqs(unittest.TestCase):
    """
    There are a total of num_courses courses you have to take, labeled from 0 to num_courses - 1.
    You are given an array prerequisites where prerequisites[i] = [ai, bi]
    meaning that you must take course bi first if you want to take course ai.

    For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
    Return the ordering of courses you should take to finish all courses.
    If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

    Input: num_courses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
    Output: [0,2,1,3]
    Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
    So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
    """
    def get_order(self, num_courses, prerequisites):
        """
        :type num_courses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        # map courses to preqs and preqs to courses
        course_preq_dic = {course: set() for course in range(num_courses)}
        preq_course_dic = collections.defaultdict(set)
        for course, preq in prerequisites:
            course_preq_dic[course].add(preq)
            preq_course_dic[preq].add(course)

        # add any courses without preqs to new taken_q
        taken_q = collections.deque([])
        for course, preq in course_preq_dic.items():
            if len(preq) == 0:
                taken_q.append(course)

        # go through q to see if we can take expected num of courses
        taken = []
        while taken_q:
            course = taken_q.popleft()
            taken.append(course)
            if len(taken) == num_courses:
                return taken
            # use preq_course_dic to check every dependent course that had the course we just took as a preq
            for dependent in preq_course_dic[course]:
                # remove the taken course from the course_preq_dic for any dependent courses
                course_preq_dic[dependent].remove(course)
                # if dependent course no longer has any preqs then we can add it as course to take
                if not course_preq_dic[dependent]:
                    taken_q.append(dependent)
        return False

    def test_prereqs(self):
        prereqs = [[1,0],[2,0],[3,1],[3,2]]
        acceptable_results = [[0,1,2,3], [0,2,1,3]]
        self.assertIn(self.get_order(len(prereqs), prereqs), acceptable_results)