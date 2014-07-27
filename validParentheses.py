class Solution:
    # use stack
    # @return a boolean
    def isValid(self, s):
        if s == '': return None
        stack = []
        for bracket in s:
            if bracket in ['(','{', '[']:
                stack.append(bracket)
                print 's', stack
            else:
                print bracket
                print len(stack)
                if len(stack) == 0: return False
                current = stack.pop()
                print 'c',current
                if current == '(' and bracket != ')':
                    return False
                elif current == '{' and bracket != '}':
                    return False
                elif current == '[' and bracket != ']':
                    return False
        if len(stack) != 0: return False
        return True
print Solution().isValid('()')