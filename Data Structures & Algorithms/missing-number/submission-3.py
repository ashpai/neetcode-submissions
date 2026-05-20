class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # sub-optimal
        # o(n) time 
        # o(n) space for seen dictionary
        # n = len(nums)
        # seen ={i: 0 for i in range(n+1)}

        # for num in nums:
        #     seen[num] += 1
        
        # for key, value in seen.items():
        #     if value ==0:
        #         return key
        # n = len(nums)
        # nums.sort()
        # for i in range(n):
        #     if nums[i] != i:
        #         return i
        # return n
        sum_n = 0
        n = len(nums)
        for i in range(n+1):
            sum_n += i
        
        return sum_n - sum(nums)


        