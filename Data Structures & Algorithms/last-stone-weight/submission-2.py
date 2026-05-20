from heapq import heapify, heappush, heappop
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # not needed due to constraints
        # if not stones:
        #     return 0
        # create and add to heap 

        # till size(heap) > 1 
        # pop two and smash 
        stone_heap = [-1 * stone for stone in stones]
        heapify(stone_heap)

        while len(stone_heap) > 1:
            top = heappop(stone_heap)
            second = heappop(stone_heap)

            diff = abs(top) - abs(second)

            if diff != 0:
                heappush(stone_heap, -diff)
        
        return -1*  stone_heap[0] if len(stone_heap) != 0 else 0


        