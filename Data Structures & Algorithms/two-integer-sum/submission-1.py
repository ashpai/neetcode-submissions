class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for index, value in enumerate(nums):
            complement = target - value 
            if complement in seen:
                return [index, seen[complement]] if index <= seen[complement] else [seen[complement], index]
            
            seen[value] = index

        # should not get here.
        return []

        