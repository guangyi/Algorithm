class Solution:
    # @return a list of lists of string
    def solveNQueens(self, n):
        return self.solve(0, [], n, 0)
    
    def solve(self, row, queenPosition, n, result):
        if row == n:# done, every queen is valid, add to result
            result += 1
            return result
        else:
            for col in range(0, n):
                if row == 0: queenPosition = []
                if self.isValid(row, col, queenPosition):
                    # queenPosition: index stands for row, elements stans for col: [1] means [0][1] is queen
                    queenPosition.append(col)
                    result = self.solve(row + 1, queenPosition, n, result)
            return result   
                    
    def isValid(self, row, col, queenPosition):
        if col in queenPosition: return False # at the same col return False
        if abs(col - (len(queenPosition) - 1)) == 1: return False # at corner of previou queen position return False
        return True