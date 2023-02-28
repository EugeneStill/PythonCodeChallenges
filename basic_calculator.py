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
                print("IDX {}".format(i))
                # if digit, add to running num
                if s[i].isdigit():
                    print("VAL {} IS DIGIT. NUM BEFORE {}".format(s[i], num))
                    # *10 for cases when there is more than one digit in a row in the string.  eg. 12, 123, etc.
                    num = num * 10 + int(s[i])
                    print("NUM AFTER {}".format(num))
                # if op, call update with previous op & running num then set op value for next update
                elif s[i] in "+-*/":
                    print("GOT s[i] {} CALLING UPDATE W OP {} NUM {}".format(s[i], op, num))
                    update(op, num)
                    num, op = 0, s[i]
                    print("FOUND OP {} NEW NUM {} STACK {}".format(op, num, str(stack)))
                # handle ( call calc to start new expression
                elif s[i] == "(":
                    print("*** HIT OPENING (.  STARTING NEW STACK AT IDX {}".format(i))
                    num, next_expression_idx = calc(i + 1)
                    # go back one for i so that when we increment i at end of loop we will start next itertation at next_expression_idx
                    i = next_expression_idx - 1
                    print("*** GOT J {}. SETTING IDX TO {}".format(next_expression_idx, i))
                    print("( NUM {} J {} IDX {} STACK {}".format(num, next_expression_idx, i, str(stack)))
                # handle )  return sum of stack for expression
                elif s[i] == ")":
                    update(op, num)
                    print("HIT CLOSING ).  UPDATING STACK " + str(stack))
                    return sum(stack), i + 1
                i += 1
            print("END OP {} NUM {}".format(op, num))
            update(op, num)
            print("END {}".format(str(stack)))
            return sum(stack)

        print("\n" + s)
        return calc(0)

    def test_calc(self):
        # num = "(1*(4+5+2)-3)+(6+8)+(5+7)"
        # output = 34
        num = "2+4*3"
        output = 14
        self.assertEqual(self.calculate(num), output)

# LOGGING
# (1*(4+5+2)-3)+(6+8)+(5+7)
# IDX 0
# *** HIT OPENING (.  STARTING NEW STACK AT IDX 0
# IDX 1
# VAL 1 IS DIGIT. NUM BEFORE 0
# NUM AFTER 1
# IDX 2
# GOT s[i] * CALLING UPDATE W OP + NUM 1
# FOUND OP * NEW NUM 0 STACK [1]
# IDX 3
# *** HIT OPENING (.  STARTING NEW STACK AT IDX 3
# IDX 4
# VAL 4 IS DIGIT. NUM BEFORE 0
# NUM AFTER 4
# IDX 5
# GOT s[i] + CALLING UPDATE W OP + NUM 4
# FOUND OP + NEW NUM 0 STACK [4]
# IDX 6
# VAL 5 IS DIGIT. NUM BEFORE 0
# NUM AFTER 5
# IDX 7
# GOT s[i] + CALLING UPDATE W OP + NUM 5
# FOUND OP + NEW NUM 0 STACK [4, 5]
# IDX 8
# VAL 2 IS DIGIT. NUM BEFORE 0
# NUM AFTER 2
# IDX 9
# HIT CLOSING ).  UPDATING STACK [4, 5, 2]
# *** GOT J 10. SETTING IDX TO 9
# ( NUM 11 J 10 IDX 9 STACK [1]
# IDX 10
# GOT s[i] - CALLING UPDATE W OP * NUM 11
# FOUND OP - NEW NUM 0 STACK [11]
# IDX 11
# VAL 3 IS DIGIT. NUM BEFORE 0
# NUM AFTER 3
# IDX 12
# HIT CLOSING ).  UPDATING STACK [11, -3]
# *** GOT J 13. SETTING IDX TO 12
# ( NUM 8 J 13 IDX 12 STACK []
# IDX 13
# GOT s[i] + CALLING UPDATE W OP + NUM 8
# FOUND OP + NEW NUM 0 STACK [8]
# IDX 14
# *** HIT OPENING (.  STARTING NEW STACK AT IDX 14
# IDX 15
# VAL 6 IS DIGIT. NUM BEFORE 0
# NUM AFTER 6
# IDX 16
# GOT s[i] + CALLING UPDATE W OP + NUM 6
# FOUND OP + NEW NUM 0 STACK [6]
# IDX 17
# VAL 8 IS DIGIT. NUM BEFORE 0
# NUM AFTER 8
# IDX 18
# HIT CLOSING ).  UPDATING STACK [6, 8]
# *** GOT J 19. SETTING IDX TO 18
# ( NUM 14 J 19 IDX 18 STACK [8]
# IDX 19
# GOT s[i] + CALLING UPDATE W OP + NUM 14
# FOUND OP + NEW NUM 0 STACK [8, 14]
# IDX 20
# *** HIT OPENING (.  STARTING NEW STACK AT IDX 20
# IDX 21
# VAL 5 IS DIGIT. NUM BEFORE 0
# NUM AFTER 5
# IDX 22
# GOT s[i] + CALLING UPDATE W OP + NUM 5
# FOUND OP + NEW NUM 0 STACK [5]
# IDX 23
# VAL 7 IS DIGIT. NUM BEFORE 0
# NUM AFTER 7
# IDX 24
# HIT CLOSING ).  UPDATING STACK [5, 7]
# *** GOT J 25. SETTING IDX TO 24
# ( NUM 12 J 25 IDX 24 STACK [8, 14]
# END OP + NUM 12
# END [8, 14, 12]