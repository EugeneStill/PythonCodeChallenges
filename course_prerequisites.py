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
        # preq dict {course: prerequisites}
        preq = {course: set() for course in range(num_courses)}
        graph = collections.defaultdict(set)

        # update dict & build graph
        for course, prereq in prerequisites:
            preq[course].add(prereq)
            graph[prereq].add(course)

        # create q for BFS
        q = collections.deque([])
        # find a vertex in the graph where we can start BFS. use courses that have no prereqs.
        for course, prereq in preq.items():
            if len(prereq) == 0:
                q.append(course)

        # do BFS
        taken = []
        while q:
            course = q.popleft()
            taken.append(course)
            # If we have visited the num_courses we're done.
            if len(taken) == num_courses:
                return taken
            # For neighboring courses.
            for neighbor in graph[course]:
                # If the course we've just taken was a prereq for neighbor, remove it from neighbor's prereqs.
                preq[neighbor].remove(course)
                # If we've taken all of the preqs for the neighbor's course,
                # add neighbor node to q so we can take that course
                if not preq[neighbor]:
                    q.append(neighbor)
        # If we didn't hit num_courses in BFS, we know we can't take all of the courses.
        return []

    def test_prereqs(self):
        prereqs = [[1,0],[2,0],[3,1],[3,2]]
        acceptable_results = [[0,1,2,3], [0,2,1,3]]
        self.assertIn(self.get_order(len(prereqs), prereqs), acceptable_results)