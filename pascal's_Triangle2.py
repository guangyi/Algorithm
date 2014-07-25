class Solution:
    # @return a list of integers
    # just return different format with pascal's triangle 1
    def getRow(self, rowIndex):
        result = [1]
        for index in range(1, rowIndex + 1):
            newResult = []
            for i in range(0, len(result)):
                if i + 1 < len(result):
                    newResult.append(result[i] + result[i + 1])
            newResult.insert(0, 1)
            newResult.append(1)
            result = newResult
        return result