class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        ROWS, COLS = len(grid), len(grid[0])

        def get_neighbors(point: List[int]):
            dir_x = [0, -1, 0, 1]
            dir_y = [-1, 0, 1, 0]
            result = []

            for i in range(len(dir_x)):
                n_r = point[0] + dir_x[i]
                n_c = point[1] + dir_y[i]

                if (n_r >= 0 and n_r < ROWS) and (n_c >=0 and n_c < COLS) and grid[n_r][n_c] == INF:
                    result.append([n_r,n_c])
            return result
        
        q = deque([])
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    q.append([i, j])
        
        while q:
            point = q.popleft()

            for neighbor in get_neighbors(point):
                grid[neighbor[0]][neighbor[1]]= grid[point[0]][point[1]] + 1 
                q.append(neighbor)
        

        