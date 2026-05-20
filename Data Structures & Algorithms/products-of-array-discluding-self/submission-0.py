class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] *len(nums)

        multiplier = 1 
        for i in range(len(nums)-1, -1, -1):
            result[i] *= multiplier
            multiplier *= nums[i]
        
        multiplier = 1
        for i in range(len(result)):
            result[i] *= multiplier
            multiplier *= nums[i]
        
        return result
        