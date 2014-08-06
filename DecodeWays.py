# Be careful with 0!!!!!!
class Solution:
    # @param s, a string
    # @return an integer
    def numDecodings(self, s):
        if s == '' or s =='0': return 0
        result = [1 for i in range(0, len(s) + 1)]
        if s[0] == '0': result[1] = 0
        for index in range(2, len(result)):
            prevOne = result[index - 1] if s[index - 1] != '0' else 0
            prevTwo = result[index - 2] if int(s[index - 2] + s[index - 1]) <= 26 and s[index - 2] != '0' else 0
            result[index] = prevOne + prevTwo
        return result[-1]


print Solution().numDecodings('0113') # 0
