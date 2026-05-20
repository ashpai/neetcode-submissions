class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # if not nums:
        #     return 0
        # max_range, min_range = max(nums), min(nums)

        # counts = [0] * (max_range - min_range + 1)

        # for num in nums:
        #     counts[num - min_range] += 1

        # largest_conseq = 0

        # for i in range(len(counts)):
        #     if counts[i] > 0:
        #         j = i 
        #         while j < len(counts) and counts[j] != 0:
        #             j += 1
        #         largest_conseq = max(largest_conseq, j-i)
        #         i = j
        # return  largest_conseq
        seen = set()
        for num in nums:
            if num in seen:
                continue
            seen.add(num)
        
        longest_sequence = 0
        for num in nums:
            if num - 1 not in seen:
                start = num
                sequence = 0
                while start in seen:
                    sequence += 1
                    longest_sequence = max(longest_sequence, sequence)
                    start += 1

        return longest_sequence 

         
        