class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix2(self, matrix, target):
        cols = len(matrix[0])
        rows = len(matrix)
        for row in range(rows - 1, -1, -1):
            if target == matrix[row][0]:return True
            if target > matrix[row][0]:
                if target in matrix[row]: return True
                else: return False
        return False
    
    # This method is little bit faster
    def searchMatrix(self, matrix, target):
        rows = len(matrix) - 1
        return self.search(matrix, 0, rows, target)
    def search(self, matrix, start, end, target):
        if start > end: return False
        mid = start + (end - start) / 2
        if target < matrix[mid][0]: return self.search(matrix, start, mid - 1, target)
        elif target > matrix[mid][-1]: return self.search(matrix, mid + 1, end, target)
        elif target in matrix[mid]: return True
        else: return False