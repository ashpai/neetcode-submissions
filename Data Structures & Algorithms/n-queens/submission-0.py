class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.' for col in range(n)] for row in range(n)]
        result = []
        
        def canPlace(row: int, col: int, board:List[List[int]]):
            c_row, c_col = row, col

            while row >=0 and col >= 0:
                if board[row][col]=='Q': return False
                row -= 1
                col -= 1
            
            row, col = c_row, c_col
            while row < n and col >= 0:
                if board[row][col]=='Q': return False
                row += 1
                col -= 1
            
            col = c_col
            row = c_row
            while col >= 0:
                if board[row][col]=='Q': return False
                col -= 1
            
            return True
        def backtrack(col: int, board:List[List[int]]):
            if col == n:
                result.append([''.join(row) for row in board])
                return
            
            for row in range(n):
                if canPlace(row, col, board):
                    board[row][col] = 'Q'
                    backtrack(col+1, board)
                    board[row][col] = '.'
        
        backtrack(0, board)
        return result

        