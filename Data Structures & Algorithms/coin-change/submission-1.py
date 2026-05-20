class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def helper(amount: int):
            if amount == 0:
                return 0
            if amount < 0:
                return -1
            
            if amount in memo:
                return memo[amount]
            
            min_ways = float('inf')
            for coin in coins:
                sub_problem = helper(amount - coin)
                if sub_problem > -1:
                    min_ways = min(min_ways, 1 + sub_problem)
            memo[amount] = min_ways if min_ways != float('inf') else -1 
            return memo[amount]
        return helper(amount)
