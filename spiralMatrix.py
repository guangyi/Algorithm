'''
!!! don't forget to return [] when matrix is []
in this case, numOfCol == None becuase there is no matrix[0]
'''
class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        numOfRow = len(matrix)
        if numOfRow == 0: return []
        numOfCol = len(matrix[0])
        colStartLimit = 0
        rowStartLimit = 0
        colLimit = numOfCol - 1
        rowLimit = numOfRow - 1
        row = col = 0
        result = []
        flag = -1
        while len(result) < numOfRow * numOfCol:
            flag = -flag
            while col >= colStartLimit and col <= colLimit and colStartLimit <= colLimit:
                result.append(matrix[row][col])
                col += flag
            if flag == 1: 
                rowStartLimit += 1
                col = colLimit
            else: 
                rowLimit -= 1
                col = colStartLimit
            row += flag
            while row >= rowStartLimit and row <= rowLimit and rowStartLimit <= rowLimit:
                result.append(matrix[row][col])
                row += flag
            if flag == 1: 
                colLimit -= 1
                row = rowLimit
            else:
                colStartLimit += 1
                row = rowStartLimit
            col += -flag
        return result


print Solution().spiralOrder([[1,2,3],[4,5,6],[7,8,9]])
print Solution().spiralOrder([[1,2],[3,4]])
print Solution().spiralOrder([[12],[3]])