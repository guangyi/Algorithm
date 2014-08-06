class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        check = {}
        for unitRow in range(3, 10, 3):
            for unitCol in range(3, 10, 3):
                temp = []
                for row in range(unitRow - 3, unitRow):
                    for col in range(unitCol - 3, unitCol):
                        currentNum = board[row][col]
                        if currentNum == '.': continue
                        if currentNum in temp:
                            return False
                        else:
                            temp.append(currentNum)
                            if currentNum not in check:
                                check[currentNum] = [[row], [col]]
                            else:
                                if row in check[currentNum][0]: return False
                                if col in check[currentNum][1]: return False
                                check[currentNum][0].append(row)
                                check[currentNum][1].append(col)
        return True