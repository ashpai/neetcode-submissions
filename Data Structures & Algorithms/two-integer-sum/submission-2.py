class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for index, value in enumerate(nums):
            complement = target - value 
            if complement in seen:
                return [min(index, seen[complement]), max(index, seen[complement]),] 
            seen[value] = index

        # should not get here.
        return []

        