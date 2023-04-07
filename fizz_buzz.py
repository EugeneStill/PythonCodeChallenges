import unittest


class FizzBuzz(unittest.TestCase):
    def fizz_buzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        answer = []
        for i in range(1, n+1):
            ans = ""
            if i % 3 == 0:
                ans += "Fizz"
            if i % 5 == 0:
                ans += "Buzz"
            if ans == "":
                ans += str(i)
            answer.append(ans)
        return answer

    def test_fb(self):
        output_15 = ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
        self.assertEqual(self.fizz_buzz(15), output_15)