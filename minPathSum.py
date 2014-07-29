class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    '''
Created on Jul 24, 2014

@author: zhouguangyi2009
'''
import sys
class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    
    # Primary way!!!
    def minPathSumFast(self, grid):
        row = len(grid)
        col = len(grid[0])
        result = [sys.maxint for i in range(0, col)]
        result[0] = grid[0][0]
        for i in range(0, row):
            if i != 0: result[0] = result[0] + grid[i][0]
            for j in range(1, col):
                result[j] = min(result[j - 1], result[j]) + grid[i][j]
        return result[col - 1]
    
    # two dimension array-- more clear
    def minPathSum(self, grid):
        y = len(grid)
        x = len(grid[0])
        result = [[0 for i in range(0, x)] for j in range(0, y)] 
        result[0][0] = grid[0][0]
        for i in range(1, y):
            result[i][0] = result[i - 1][0] + grid[i][0]
        for j in range(1, x):
            result[0][j] = result[0][j - 1] + grid[0][j]
        for i in range(1, y):
            for j in range(1, x):
                result[i][j] = min(result[i - 1][j], result[i][j - 1]) + grid[i][j]
        return result[y - 1][x - 1]
    
    def minSum(self, indexX, indexY, grid):
        if indexX == 0 and indexY == 0:
            return grid[0][0]
        if indexY == 0:
            return self.minSum(indexX - 1, indexY, grid) + grid[indexY][indexX]
        if indexX == 0:
            return self.minSum(indexX, indexY - 1, grid) + grid[indexY][indexX]
        return min(self.minSum(indexX- 1, indexY, grid), self.minSum(indexX, indexY - 1, grid)) + grid[indexY][indexX]
            
print Solution().minPathSumRe([[1,2,3],[1,2,3]]) #7
print Solution().minPathSumRe([[1,2,3],[3,4,1],[1,1,1]])#7
print Solution().minPathSum([[1,2,3],[1,2,3]]) #7