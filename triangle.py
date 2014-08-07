class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        if len(triangle) == 0: return 0
        numOfRow = len(triangle)
        numOfCol = len(triangle[-1]) # last row's column number
        result = [[None for i in range(0, numOfCol)] for j in range(0, numOfRow)]
        result[0][0] = triangle[0][0]
        for row in range(1, numOfRow):
            for col in range(0, len(triangle[row])):
                # first element only comes from previous first element
                if col == 0: sameIndex = minusOneIndex = result[row - 1][0]
                # last element only comes from previous last element
                elif col == len(triangle[row]) - 1: minusOneIndex = sameIndex = result[row - 1][len(triangle[row - 1]) - 1]
                else:
                    sameIndex = result[row - 1][col]
                    minusOneIndex = result[row - 1][col - 1]
                result[row][col] = min(sameIndex, minusOneIndex) + triangle[row][col]
        return min(result[numOfRow - 1])