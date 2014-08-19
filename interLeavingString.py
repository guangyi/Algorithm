class Solution:
    # @return a boolean
    def isInterleave(self, s1, s2, s3):
        if s1 == '': return s2 == s3
        if s2 == '': return s1 == s3
        col = len(s1)
        row = len(s2)
        if col + row != len(s3): return False
        match = [[True for i in range(0, col + 1)] for i in range(0, row + 1)]
        
        for i in range(1, col + 1):
            if s1[i - 1] != s3[i - 1]:
                match[0][i] =  False
            else:
                match[0][i] = match[0][i - 1]
        for i in range(1, row + 1):
            if s2[i - 1] != s3[i - 1]:
                match[i][0] = False
            else: match[i][0] =  match[i - 1][0]
        
        for i in range(1, row ):
            for j in range(1, col):
                match[i][j] = (match[i][j - 1] and s3[i + j - 1] == s1[j]) or (match[i - 1][j] and s3[i + j - 1] == s2[i])
        print match
        return match[row][col]