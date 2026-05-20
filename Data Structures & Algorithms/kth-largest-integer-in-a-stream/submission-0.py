from heapq import heapify, heappop
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        

    def add(self, val: int) -> int:
        self.nums.append(val)
        max_h =[-num for num in self.nums]
        heapify(max_h)


        result = 0
        for i in range(self.k):
            result = heappop(max_h)
        return -result




        
