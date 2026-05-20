class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = []
        carry = 0

        for i in range(len(digits) - 1, -1, -1):
            if i == len(digits) - 1:
                carry += 1
            sum_digit, carry = (carry + digits[i]) %10, (carry + digits[i]) // 10
            result.append(sum_digit)
        
        if carry > 0: result.append(carry)
        result.reverse()
        return result
        