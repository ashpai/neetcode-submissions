class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        seen ={i: 0 for i in range(n+1)}

        for num in nums:
            seen[num] += 1
        
        for key, value in seen.items():
            if value ==0:
                return key


        