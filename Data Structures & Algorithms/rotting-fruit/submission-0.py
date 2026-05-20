from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n_r, n_c = len(grid), len(grid[0])

        q = deque([])
        fresh_count = 0
        for i in range(n_r):
            for j in range(n_c):
                if grid[i][j] == 2:
                    q.append(([i,j], 0))
                if grid[i][j] == 1:
                    fresh_count += 1 
        
        def get_neighbors(point: List[int])-> List[List[int]]:
            total_rows, total_columns = len(grid), len(grid[0])
            dir_x = [0, -1, 0, 1]
            dir_y = [-1, 0, 1 , 0]

            result =[]
            for i in range(len(dir_x)):
                new_r = point[0] + dir_x[i]
                new_c = point[1] + dir_y[i]

                if (new_r >= 0 and new_r < total_rows) and (new_c >= 0 and new_c < total_columns):
                    if grid[new_r][new_c] == 1:
                        result.append([new_r,new_c])
            return result
        total_time = 0
        while q:
            item, time = q.popleft()
            total_time = max(total_time, time)

            for neighbor in get_neighbors(item):
                grid[neighbor[0]][neighbor[1]] = 2
                q.append((neighbor, time + 1))
                fresh_count -= 1

        return total_time if fresh_count == 0 else -1  



                






        