class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        row_zeros = set()
        col_zeros = set()

        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j] == 0:
                    row_zeros.add(i)
                    col_zeros.add(j)
        
        for i in range(ROWS):
            for j in range(COLS):
                if i in row_zeros or j in col_zeros:
                    matrix[i][j] = 0
   