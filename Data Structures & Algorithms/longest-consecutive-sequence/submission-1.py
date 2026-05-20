class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        max_range, min_range = max(nums), min(nums)

        counts = [0] * (max_range - min_range + 1)

        for num in nums:
            counts[num - min_range] += 1

        largest_conseq = 0

        for i in range(len(counts)):
            if counts[i] > 0:
                j = i 
                while j < len(counts) and counts[j] != 0:
                    j += 1
                largest_conseq = max(largest_conseq, j-i)
                i = j
        return  largest_conseq
         
        