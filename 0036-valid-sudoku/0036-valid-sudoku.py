class Solution(object):
    def isSafe(self,board,row,col,dig):
        s_dig=str(dig)
        #Horizontally:
        for j in range(0,9):
            if (board[row][j]==s_dig):
                return False
        
        # Vertically:
        for i in range(0,9):
            if (board[i][col]==s_dig):
                return False

        #IN a Grid:
        sr=(row//3)*3
        sc=(col//3)*3
        for i in range(sr,sr+3):
            for j in range(sc,sc+3):
                if board[i][j]==s_dig:
                    return False
        return True

    def isValidSudoku(self, board):
        # Loop through every single cell on the board
        for row in range(9):
            for col in range(9):
                # If there's an existing digit, check if it breaks Sudoku rules
                if board[row][col] != ".":
                    val = board[row][col]
                    
                    # Temporarily clear the cell so it doesn't match against itself
                    board[row][col] = "."
                    
                    # Use your exact loop validation structure
                    if not self.isSafe(board, row, col, val):
                        return False # Found a duplicate, invalid sudoku!
                        
                    # Restore the value back to the board
                    board[row][col] = val
                    
        return True



        