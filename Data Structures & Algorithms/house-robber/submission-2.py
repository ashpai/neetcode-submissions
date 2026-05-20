class Solution:
    def rob(self, nums: List[int]) -> int:

        memo ={}
        def helper(index: int):
            if index >= len(nums):
                return 0
            if index in memo:
                return memo[index]
            
            max_booty = float('-inf')
            for i in range(index, len(nums)):
                sub_problem = helper(i + 2)
                max_booty = max(max_booty, nums[i] + sub_problem)
            
            memo[index] = max_booty
            return memo[index]
        return helper(0)


        