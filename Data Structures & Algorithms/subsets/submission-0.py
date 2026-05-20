class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def dfs(nums, index, current):
            if index == len(nums):
                result.append(current[:])
                return
            
            #dont pick and recurse 
            dfs(nums, index+1, current)

            #pick and recurse
            current.append(nums[index])
            dfs(nums, index+1, current)
            current.pop()

        dfs(nums, 0, [])
        return result
        