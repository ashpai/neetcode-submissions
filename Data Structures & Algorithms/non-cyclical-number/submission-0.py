class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n > 1:
            sum = 0
            while n > 0:
                sum += (n % 10) ** 2
                n = n // 10
            
            if sum in seen:
                return False
            seen.add(sum)
            n = sum

        return True
        