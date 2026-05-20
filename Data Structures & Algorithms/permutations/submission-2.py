class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def dfs(current, picked):
            if len(current) == len(nums):
                result.append(current.copy())
                return
            
            for i in range(len(nums)):
                if not picked[i]:
                    picked[i] = True
                    current.append(nums[i])
                    dfs(current, picked)
                    current.pop()
                    picked[i] = False
        picked = [False] * len(nums)
        if not nums:
            return []
        dfs([], picked)
        return result
        