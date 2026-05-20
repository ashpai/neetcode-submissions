class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def dfs(current):
            if len(current) == len(nums):
                result.append(current.copy())
                return
            
            for i in range(len(nums)):
                if nums[i] not in current:
                    current.append(nums[i])
                    dfs(current)
                    current.pop()
        dfs([])
        return result
        