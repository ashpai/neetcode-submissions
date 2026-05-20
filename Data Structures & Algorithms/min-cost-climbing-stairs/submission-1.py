class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = [-1 for i in range(len(cost)+1)]

        # def helper(n: int) -> int:
        #     if n <= 1:
        #         memo[n] = 0
        #         return memo[n]
        #     if memo[n] != -1:
        #         return memo[n]
            
        #     memo[n] = min(helper(n-1)+ cost[n-1], helper(n-2)+ cost[n-2])
        #     return memo[n]
        
        # return helper(len(cost))

        memo[0], memo[1] = 0, 0
        for i in range(2,len(memo)):
            memo[i] = min (memo[i-1] + cost[i-1], memo[i-2] + cost[i-2])
        
        return memo[-1]


        