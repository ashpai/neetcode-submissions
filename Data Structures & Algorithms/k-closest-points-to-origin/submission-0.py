from heapq import heapify, heappop, heappush
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        result = []
        heapify(h)
        def origin_distance(point: List[int]) -> int:
            return (point[0]**2 + point[1]**2) 

        for point in points:
            heappush(h, (origin_distance(point), point))
        
        for i in range(k):
            result.append(heappop(h)[1])
        
        return result
        