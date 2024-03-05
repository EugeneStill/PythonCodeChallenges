import unittest
from ddt import ddt, data


class FizzBuzz():

    def fizz_buzz(self, num):
        answer = []
        for n in range(1, num + 1):
            if n % 3 == 0 and n % 5 == 0:
                answer.append("FizzBuzz")
            elif n % 3 == 0:
                answer.append("Fizz")
            elif n % 5 == 0:
                answer.append("Buzz")
            else:
                answer.append(str(n))
        return answer


@ddt
class TestFizzBuzz(unittest.TestCase):

    @data(
        {"num": 15, "expected": ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13",
        "14", "FizzBuzz"]},
        {"num": 3, "expected": ["1", "2", "Fizz"]},
        {"num": 5, "expected": ["1", "2", "Fizz", "4", "Fizz"]},
    )
    # if we use dict as input, then don't use unpack decorator
    def test_fizz_buzz(self, data):
        fb = FizzBuzz()
        actual_result = fb.fizz_buzz(data["num"])
        expected_result = data["expected"]
        self.assertEqual(actual_result, expected_result, f"Expected {expected_result}, Got {actual_result}")



# import unittest
# from ddt import ddt, data, unpack
#
#
# class FizzBuzz():
#
#     def fizz_buzz(self, num):
#         print("num is " + str(num))
#         answer = []
#         for n in range(1, num + 1):
#             if n % 3 == 0 and n % 5 == 0:
#                 answer.append("FizzBuzz")
#             elif n % 3 == 0:
#                 answer.append("Fizz")
#             elif n % 5 == 0:
#                 answer.append("Buzz")
#             else:
#                 answer.append(str(n))
#         return answer
#
#
# @ddt
# class TestFizzBuzz(unittest.TestCase):
#
#     @data(
#         {"num": 15, "expected_result": ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]},
#     )
#
      # if we want to use the individual keys from the dict without accessing them from the dict inside the method
      # then we can use the unpack decorator
#     @unpack
#     def test_fizz_buzz(self, num, expected_result):
#         fb = FizzBuzz()
#         actual_result = fb.fizz_buzz(num)
#         self.assertEqual(actual_result, expected_result, f"Expected {expected_result}, Got {actual_result}")
