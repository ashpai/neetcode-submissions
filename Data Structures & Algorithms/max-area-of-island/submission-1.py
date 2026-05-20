class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        no_rows, no_cols = len(grid), len(grid[0])
        def bfs(start: List[int]) -> int:
            def get_neighbors(point: List[int]) -> List[List[int]]:
                dir_x = [0, -1, 0, 1]
                dir_y = [-1, 0, 1, 0]
                result =[]

                for i in range(len(dir_x)):
                    n_r = point[0] + dir_x[i]
                    n_c = point[1] + dir_y[i]

                    if (n_r >= 0 and n_r < no_rows) and (n_c >=0 and n_c < no_cols) and grid[n_r][n_c] == 1:
                        result.append([n_r,n_c])
                
                return result
            q = deque([start])
            # mark seen
            grid[start[0]][start[1]]=0
            area = 1
            while q:
                item = q.popleft()

                for neighbor in get_neighbors(item):
                    q.append(neighbor)
                    # mark seen
                    grid[neighbor[0]][neighbor[1]]=0
                    area += 1
            return area

        
        def dfs(start: List[int]) -> int:
            def get_neighbors(point: List[int]) -> List[List[int]]:
                dir_x = [0, -1, 0, 1]
                dir_y = [-1, 0, 1, 0]
                result =[]

                for i in range(len(dir_x)):
                    n_r = point[0] + dir_x[i]
                    n_c = point[1] + dir_y[i]

                    if (n_r >= 0 and n_r < no_rows) and (n_c >=0 and n_c < no_cols) and grid[n_r][n_c] == 1:
                        result.append([n_r,n_c])
                
                return result
            if grid[start[0]][start[1]] == 0:
                return 0
            
            grid[start[0]][start[1]] = 0
            area = 1 
            for neighbor in get_neighbors(start):
                area += dfs(neighbor)
            return area 
        max_area = 0
        for i in range(no_rows):
            for j in range(no_cols):
                if grid[i][j] == 1:
                    area = dfs([i,j])
                    max_area = max(max_area, area)
        return max_area

        