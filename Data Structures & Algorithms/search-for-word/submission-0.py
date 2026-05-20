class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        def dfs(row, col, index) -> bool:
            if index == len(word):
                return True
            if row < 0 or row == ROWS or col < 0 or col == COLS or board[row][col] != word[index]:
                return False

            tmp = board[row][col]
            board[row][col] = "#"
            found = dfs(row+1, col, index+1) or dfs(row-1, col, index+1) or dfs(row, col+1, index+1) or dfs(row, col-1, index+1)
            board[row][col] = tmp
            return found

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True

        return False 
        


        