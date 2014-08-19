class Solution:
    # @return a list of integers
    def grayCode(self, n):
        if n == 0: return [0]
        init = ['0','1']
        index = 1
        while index < n:
            result = []
            for item in init:
                result.append('0' + item)
            init.reverse()
            for item in init:
                result.append('1' + item)
            init = result
            index += 1
        newInit = []
        for item in init:
            newInit.append(int(item, 2))
        return newInit
        
Solution().grayCode(3)
Solution().grayCode(1)
Solution().grayCode(6)