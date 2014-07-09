'''
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Some examples:
  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
'''
#lambda!!!!!!
class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        stack = []
        ops={'+':(lambda x,y:x+y),
            '-':(lambda x,y:x-y),
            '*':(lambda x,y:x*y),
            '/':(lambda x,y:x/y if x/y>=0 or x%y==0 else x/y+1)}
        for token in tokens:
            if token in ops:
                a=stack.pop()
                b=stack.pop()
                stack.append(ops[token](b,a))
            else:
                stack.append(int(token))
        return stack.pop()
tokens = ["2", "1", "+", "3", "*"]
print Solution().evalRPN(tokens)

tokens = ["4", "13", "5", "/", "/"]
print Solution().evalRPN(tokens)