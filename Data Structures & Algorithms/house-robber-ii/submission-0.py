class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def dfs(index:int, pickedFirst:bool=False):
            if index >= len(nums):
                return 0
            if index == len(nums) - 1 and pickedFirst:
                return 0
            if (index, pickedFirst) in memo:
                return memo[(index, pickedFirst)]
            
            skip = dfs(index+1, pickedFirst)

            rob = 0
            if not (index == len(nums)-1 and pickedFirst):
                rob = nums[index] + dfs(index+2, pickedFirst or index==0)
            
            memo[(index, pickedFirst)]=max(rob,skip)
            return memo[(index, pickedFirst)]
        return dfs(0, False)
        