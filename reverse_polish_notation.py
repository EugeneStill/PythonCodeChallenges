import unittest

class ReversePolishNotation(unittest.TestCase):

    def reverse_polish_notation(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for t in tokens:
            if t not in "+-*/":
                stack.append(int(t))
            else:
                r, l = stack.pop(), stack.pop()
                if t == "+":
                    stack.append(l+r)
                elif t == "-":
                    stack.append(l-r)
                elif t == "*":
                    stack.append(l*r)
                else:
                    stack.append(int(float(l)/r))
        return stack.pop()

    def test_rpn(self):
        input1 = ["2","1","+","3","*"]
        input2 = ["4","13","5","/","+"]
        input3 = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
        self.assertEqual(self.reverse_polish_notation(input1), 9)
        self.assertEqual(self.reverse_polish_notation(input2), 6)
        self.assertEqual(self.reverse_polish_notation(input3), 22)
