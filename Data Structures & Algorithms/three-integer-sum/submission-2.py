class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def two_sum(start, target):
            l, r = start, len(nums) - 1

            pairs = []
            while l < r:
                if nums[l] + nums[r] > target:
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    pairs.append([nums[l], nums[r]])
                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
            return pairs
        
        if len(nums) < 3:
            return []
        nums.sort()
        result = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            pairs = two_sum(i+1, -nums[i])
            if pairs:  
                triplets = [[nums[i]] + pair for pair in pairs]
                result.extend(triplets)
        return result

        