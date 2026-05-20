class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        no_r, no_c = len(grid), len(grid[0])

        def get_neighbors(point: List[int])-> List[List[int]]:
            dir_r =[0, 1, 0, -1]
            dir_c =[-1, 0, 1, 0]

            result =[]
            for i in range(len(dir_r)):
                n_r = point[0] + dir_r[i]
                n_c = point[1] + dir_c[i]

                if (n_r >= 0 and n_r < no_r) and (n_c >= 0 and n_c < no_c) and grid[n_r][n_c] == "1":
                    result.append([n_r,n_c]) 
            
            return result
        
        def bfs(point:List[int])->bool:
            q = deque([point])

            # mark seen
            grid[point[0]][point[1]] = "0"

            while q:
                item = q.popleft()

                for neighbor in get_neighbors(item):
                    q.append(neighbor)
                    grid[neighbor[0]][neighbor[1]] = "0"
        
        island_count = 0

        for i in range(no_r):
            for j in range(no_c):
                if grid[i][j] == "1":
                    bfs([i,j])
                    island_count += 1 
        return island_count
        