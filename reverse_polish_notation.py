import unittest
import operator

class ReversePolishNotation(unittest.TestCase):
    """
    AKA Polish postfix notation or simply postfix notation
    The valid operators are '+', '-', '*', and '/'.
    Each operand may be an integer or another expression.
    The division between two integers always truncates toward zero.
    There will not be any division by zero.
    The input represents a valid arithmetic expression in a reverse polish notation.
    The answer and all the intermediate calculations can be represented in a 32-bit integer.
    """

    def reverse_polish_notation(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        ops = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': 'custom'
        }

        stack = []

        for t in tokens:
            if t not in ops:
                stack.append(int(t))
                continue
            r, l = stack.pop(), stack.pop()
            if t == '/':
                stack.append(int(l/r))
            else:
                stack.append(ops[t](l, r))
        return stack.pop()











        #
        #
        # stack = []
        # print("\n" + str(tokens))
        # for t in tokens:
        #     if t not in "+-*/":
        #         stack.append(int(t))
        #     else:
        #         r, l = stack.pop(), stack.pop()
        #         if t == "+":
        #             stack.append(l+r)
        #         elif t == "-":
        #             stack.append(l-r)
        #         elif t == "*":
        #             stack.append(l*r)
        #         else:
        #             stack.append(int(float(l)/r))
        #     print(str(stack))
        # return stack.pop()

    def test_rpn(self):
        input1 = ["2","1","+","3","*"]
        input2 = ["4","13","5","/","+"]
        input3 = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
        self.assertEqual(self.reverse_polish_notation(input1), 9)
        self.assertEqual(self.reverse_polish_notation(input2), 6)
        self.assertEqual(self.reverse_polish_notation(input3), 22)

# LOGGING
# ['2', '1', '+', '3', '*']
# [2]
# [2, 1]
# [3]
# [3, 3]
# [9]
#
# ['4', '13', '5', '/', '+']
# [4]
# [4, 13]
# [4, 13, 5]
# [4, 2]
# [6]
#
# ['10', '6', '9', '3', '+', '-11', '*', '/', '*', '17', '+', '5', '+']
# [10]
# [10, 6]
# [10, 6, 9]
# [10, 6, 9, 3]
# [10, 6, 12]
# [10, 6, 12, -11]
# [10, 6, -132]
# [10, 0]
# [0]
# [0, 17]
# [17]
# [17, 5]
# [22]