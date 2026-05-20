class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # not efficient
        # time space 
        # nums.sort() # nlog(n)
        # return nums[len(nums)-k]
        # better approach
        heapq.heapify(nums)

        while len(nums) > k:
            heapq.heappop(nums)

        return nums[0]
        