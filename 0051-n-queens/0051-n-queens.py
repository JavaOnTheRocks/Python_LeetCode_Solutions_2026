class Solution(object):
    def isSafe(self, board, row, col, n):
        # 1. Check vertical column straight up
        for i in range(row):
            if board[i][col] == 'Q':
                return False

        # 2. ADDED: Check horizontal row entirely (left and right)
        for j in range(n):
            if board[row][j] == 'Q':
                return False

        # 3. Check upper-left diagonal
        i, j = row, col
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1

        # 4. Check upper-right diagonal
        i, j = row, col
        while i >= 0 and j < n:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1

        return True

    def nQueens(self, board, row, n, ans):
        # Base Case: All queens are placed successfully
        if row == n:
            # Convert list of characters back to strings to match LeetCode format
            string_board = ["".join(r) for r in board]
            ans.append(string_board)
            return

        # Loop through all columns 'j' in the current row
        for j in range(n):
            if self.isSafe(board, row, j, n):
                board[row][j] = 'Q'                 # 1. Place the queen
                self.nQueens(board, row + 1, n, ans) # 2. Recurse to the next row
                board[row][j] = '.'    

    def solveNQueens(self, n):
        # Corrected type hint: board is initialized as list[list[str]]
        board = [["."] * n for _ in range(n)]
        ans = []
        
        # Start the recursive backtracking from row 0
        self.nQueens(board, 0, n, ans)
        return ans

        