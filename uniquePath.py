'''
Created on Jul 26, 2014

@author: zhouguangyi2009
'''
class Solution:
    # @return an integer
    # The idea is place[i][j] = place[i - 1][j] + place[i][j - 1]
    def uniquePaths(self, m, n):
        def uniquePaths(self, m, n):
        result = [1 for i in range(0, n)]
        # it only matters with the previous row, so use only one demension array is enough!!!
        for row in range(1, m):# for each row
            for col in range(1, n): # for each col start fromt the seconde one
                result[col] = result[col - 1] + result[col]
        return result[- 1]
    
    # use two dimension array
    def uniquePaths2(self, m, n):
        result = [[0 for i in range(0, n)] for i in range(0, m)]
        for i in range(0, m):# update first element in each row to 1
            result[i][0] = 1 
        for j in range(0, n):# update elements in first row to 1
            result[0][j] = 1 
        for i in range(1, m):
            for j in range(1, n):
                result[i][j] = result[i - 1][j] + result[i][j - 1]
        return result[m - 1][n - 1]