'''
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.
'''
class Solution:
    # @return a string
    def countAndSay(self, n):
        count = 1
        prevSequence = '1'
        while count < n:
            newSequence = prevDigit  = ''
            oneCounter = 0
            for digit in prevSequence:
                if prevDigit == '':
                    prevDigit = digit
                    oneCounter += 1
                elif digit == prevDigit:
                    oneCounter += 1
                else: #prevDigit != digit 
                    newSequence += str(oneCounter) + prevDigit
                    prevDigit = digit
                    oneCounter = 1
            newSequence += str(oneCounter) + prevDigit
            count += 1
            prevSequence = newSequence
        return prevSequence
print Solution().countAndSay(2)
print Solution().countAndSay(3)
print Solution().countAndSay(4)
print Solution().countAndSay(5)
print Solution().countAndSay(6)
'''
11
21
1211
111221
312211
'''