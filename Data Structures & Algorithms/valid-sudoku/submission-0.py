class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def get_box(i,j):
            if (i>= 0 and i<3) and (j>=0 and j<3):
                return 0
            elif (i>= 0 and i<3) and (j>=3 and j<6):
                return 1
            elif (i>= 0 and i<3) and (j>=6 and j<9):
                return 2
            if (i>= 3 and i<6) and (j>=0 and j<3):
                return 3
            elif (i>= 3 and i<6) and (j>=3 and j<6):
                return 4
            elif (i>= 3 and i<6) and (j>=6 and j<9):
                return 5
            if (i>= 6 and i<9) and (j>=0 and j<3):
                return 6
            elif (i>= 6 and i<9) and (j>=3 and j<6):
                return 7
            else:
                return 8
        ROWS, COLS = len(board), len(board[0])
        row_seen = [set() for i in range(ROWS)]
        col_seen = [set() for i in range(COLS)]
        box_seen = [set() for i in range(9)]

        for i in range(ROWS):
            for j in range(COLS):
                item = board[i][j]

                if item == ".":
                    continue
                if item in row_seen[i]:
                    return False
                row_seen[i].add(item)

                if item in col_seen[j]:
                    return False
                col_seen[j].add(item)

                if item in box_seen[get_box(i,j)]:
                    return False
                box_seen[get_box(i,j)].add(item)
        
        return True
        