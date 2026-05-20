class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = [-1 for i in range(len(cost)+1)]

        def helper(n: int) -> int:
            if n <= 1:
                memo[n] = 0
                return memo[n]
            if memo[n] != -1:
                return memo[n]
            
            memo[n] = min(helper(n-1)+ cost[n-1], helper(n-2)+ cost[n-2])
            return memo[n]
        
        return helper(len(cost))


        