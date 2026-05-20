class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrack(current, index):
            # if index == 0:
            #     result.append([])
            result.append(current[:]) 
            
            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i-1]:
                    continue 
                current.append(nums[i])
                backtrack(current, i + 1)
                current.pop()
            
        
        nums.sort()
        backtrack([], 0)
        return result
        