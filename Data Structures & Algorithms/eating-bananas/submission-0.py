import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canFinishInTime(eatingRate: int) -> bool:
            total = 0
            for pile in piles:
                total+= math.ceil(pile / eatingRate)
            return total <= h


        left, right = 1, max(piles)
        candidate = -1

        while left <= right:
            mid = (left + right)  // 2

            if canFinishInTime(mid):
                candidate = mid
                right = mid - 1
            else:
                left = mid + 1 
        
        return candidate



        