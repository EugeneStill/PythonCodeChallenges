import unittest


class Fibonacci(unittest.TestCase):
    """
    Input: n = 2
    Output: 1
    Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1

    Input: n = 3
    Output: 2
    Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2

    Input: n = 4
    Output: 3
    Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3
    """
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        cache = {}
        def recur_fib(n):
            if n in cache:
                print("GETTING {} FROM CACHE: {}".format(n, cache[n]))
                return cache[n]

            # n will be less than 2 when the recursive calls for 2 - 1 and 2 - 2 are mode
            if n < 2:
                print("N IS {}".format(n))
                result = n
            else:
                print("MAKING RECURSIVE CALL FOR N {}".format(n))
                result = recur_fib(n - 1) + recur_fib(n - 2)
                print("RESULT FOR N {}: {}".format(n, result))

            # use memoization (cache result for later reference)
            print("PUTTING N: {} IN CACHE".format(n))
            cache[n] = result
            return result

        return recur_fib(n)


    def test_fib(self):
        self.assertEqual(self.fib(4), 3)

# LOGGING
# MAKING RECURSIVE CALL FOR N 4
# MAKING RECURSIVE CALL FOR N 3
# MAKING RECURSIVE CALL FOR N 2
# N IS 1
# PUTTING N: 1 IN CACHE
# N IS 0
# PUTTING N: 0 IN CACHE
# RESULT FOR N 2: 1
# PUTTING N: 2 IN CACHE
# GETTING 1 FROM CACHE: 1
# RESULT FOR N 3: 2
# PUTTING N: 3 IN CACHE
# GETTING 2 FROM CACHE: 1
# RESULT FOR N 4: 3
# PUTTING N: 4 IN CACHE
