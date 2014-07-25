class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        if numRows == 0: return []
        result = [[1]] 
        currArr = result[0]
        index = 2
        for index in range(2, numRows + 1):
            newArr = []
            for i in range (0, len(currArr)):
                if i + 1 < len(currArr):
                    newArr.append(currArr[i] + currArr[i + 1])
            newArr.insert(0, 1)
            newArr.append(1)
            result.append(newArr)
            currArr = newArr
        return result
print Solution().generate(0)
print Solution().generate(2)
print Solution().generate(3)
print Solution().generate(4)
print Solution().generate(5)
'''
[]
[[1], [1, 1]]
[[1], [1, 1], [1, 2, 1]]
[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
'''