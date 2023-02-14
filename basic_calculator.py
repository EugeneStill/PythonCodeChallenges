import unittest


class Calculate(unittest.TestCase):
    """
    Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the
    result of the evaluation.

    Note: You are not allowed to use built-in functions that evaluate strings as mathematical expressions, like eval().

    """
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """

        def calc(i):
            def update(op, v):
                if op == "+": stack.append(v)
                if op == "-": stack.append(-v)
                if op == "*": stack.append(stack.pop() * v)
                if op == "/": stack.append(int(stack.pop() / v))

            # stack will contain results of operations as we traverse string so that we can return sum of stack at end
            num, stack, op = 0, [], "+"

            while i < len(s):
                print("I {}".format(i))
                if s[i].isdigit():
                    print("NUM BEFORE {}".format(num))
                    num = num * 10 + int(s[i])
                    print("NUM AFTER {}".format(num))
                elif s[i] in "+-*/":
                    update(op, num)
                    num, op = 0, s[i]
                # when we hit an opening (, call calc with the next char in s, use j to track nested ( values
                elif s[i] == "(":
                    num, j = calc(i + 1)
                    i = j - 1
                # when we hit ) we return the sum of the stack for the operation we performed
                elif s[i] == ")":
                    update(op, num)
                    print(str(stack))
                    return sum(stack), i + 1
                i += 1
            update(op, num)
            print("END {}".format(str(stack)))
            return sum(stack)

        return calc(0)

    def test_calc(self):
        input = "(1+(4+5+2)-3)+(6+8)"
        output = 23
        self.assertEqual(self.calculate(input), output)

