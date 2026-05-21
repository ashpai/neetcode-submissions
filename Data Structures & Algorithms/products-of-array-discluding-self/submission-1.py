class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []
            
        left_product = 1
        result = []
        
        """
        [1, 1, 2, 8]
        [      ,24,12 ,  8]
        """


        for i in range(len(nums)):
            result.append(left_product)
            left_product *= nums[i]

        right_product = 1

        for i in range(len(nums) - 1, -1, -1):
            result[i] *= right_product
            right_product *= nums[i]

        return result
 
        
        