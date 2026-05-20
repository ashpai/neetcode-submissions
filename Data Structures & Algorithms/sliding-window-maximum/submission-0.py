class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # result = []

        # for i in range(k-1, len(nums)):
        #     result.append(max(nums[i-k+1:i+1]))

        # return result

        l = r = 0
        q = collections.deque()
        result= []

        while r < len(nums):
            while q and nums[r] > nums[q[-1]]:
                q.pop()
            # note this is index    
            q.append(r)

            if l > q[0]:
                q.popleft()
            
            if r-l+1 >=k:
                result.append(nums[q[0]])
                l += 1
            r += 1
        return result



        