class Solution:
    # @return a list of integers
    def gray(self, result, n):
        if n <= 0: return result
        newResult = []
        if result == []:
            newResult.append('0')
            newResult.append('1')
        else:
            for item in result:
                newResult.append('0' + item)
            result.reverse()
            for item in result:
                newResult.append('1' + item)
        newResult = self.gray(newResult, n - 1)
        return newResult
                
                
    def grayCode(self, n):
        result = self.gray([], n)
        temp = []
        for item in result:
            temp.append(int(item, 2))
        print temp
Solution().grayCode(3)
Solution().grayCode(1)
Solution().grayCode(6)