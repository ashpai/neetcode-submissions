class Solution:
    def climbStairs(self, n: int) -> int:
        # memo = {}
        # def helper(n)->int:
        #     if n == 0 or n == 1:
        #         return 1 
        #     if n in memo:
        #         return memo[n]
        #     memo[n] = helper(n-1) + helper(n-2)
        #     return memo[n]
        # return helper(n)
        dp = [1 for i in range(n+1)] 

        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]
                

        