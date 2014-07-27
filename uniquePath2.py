class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    # Didn't use one demension array cause there is obstacles in
    def uniquePathsWithObstacles(self, obstacleGrid):
        if obstacleGrid[0][0] == 1: return 0
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        result = [[0 for i in range(0, col)] for i in range(0, row)]
        for i in range(0, col):
            if obstacleGrid[0][i] != 1:
                result[0][i] = 1  
            # if there is obstacle in the first row/col, the space after 
            # that obstacle can not be reached
            else: break
        for j in range(0, row):
            if obstacleGrid[j][0] != 1:
                result[j][0] = 1  
            else: break
        for i in range(1, row):
            for j in range(1, col):
                result[i][j] = result[i - 1][j] + result[i][j - 1] if obstacleGrid[i][j] != 1 else 0
        return result[row - 1][col - 1]