'''
valid_parentheses("()") # True
valid_parentheses(")(()))") # False
valid_parentheses("(") # False
valid_parentheses("(())((()())())") # True
valid_parentheses('))((') # False
valid_parentheses('())(') # False
valid_parentheses('()()()()())()(') # False
'''

def valid_parentheses(string):
    for i in range(len(string)):
        string = string.replace("()", "")
    if len(string) > 0:
        return False
    return True