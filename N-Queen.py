class Solution:
    # @return a list of lists of string
    def solveNQueens(self, n):
        result = []
        self.solve(0, [], n, result)
        return result
    def solve(self, row, queenPosition, n, result):
        if row == n:# done, every queen is valid, add to result
            temp = [] # temp to store this solution
            for i in range(0, len(queenPosition)):
                line = ''
                for j in range(0, n):
                    if j != queenPosition[i]: line = line + '.'
                    else: line = line + 'Q'
                temp.append(line)
            result.append(temp)
        else:
            for col in range(0, n):
                if row == 0: queenPosition = []
                if self.isValid(row, col, queenPosition):
                    # queenPosition: index stands for row, elements stans for col: [1] means [0][1] is queen
                    queenPosition.append(col)
                    self.solve(row + 1, queenPosition, n, result)
                
                    
    def isValid(self, row, col, queenPosition):
        if col in queenPosition: return False # at the same col return False
        if abs(col - (len(queenPosition) - 1)) == 1: return False # at corner of previou queen position return False
        return True
print Solution().solveNQueens(4) # [['.Q..', 'Q...', '...Q', '..Q.'], ['...Q', 'Q...', '.Q..', '..Q.']]
