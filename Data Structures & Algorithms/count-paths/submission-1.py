class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return self._uniquePaths(m, n, (0, 0), (m-1, n-1), {})
        # dp = [[0 for _ in range(n)] for _ in range(m)]
        
        
        # for i in range(m):
        #     for j in range(n):
        #         if i ==0 or j ==0:
        #             dp[i][j] = 1
        #         else:
        #             dp[i][j] = dp[i][j-1] + dp[i-1][j]
        
        # # for i in range(1,m):
        # #     for j in range(1,n):
        # #         dp[i][j] = dp[i][j-1] + dp[i-1][j]
        
        # return dp[m-1][n-1]
    def _uniquePaths(self, m, n, start, end, memo):
        key = start
        if key in memo:
            return memo[key]
        if start[0] < 0 or start[0] >= m or start[1] < 0 or start[1] >= n:
            return 0
        
        if start == end:
            return 1
        
        memo[key] = self._uniquePaths(m, n, (start[0]+1, start[1]), end, memo)  + self._uniquePaths(m, n, (start[0], start[1]+1), end, memo) 
    
        return memo[key]



        
