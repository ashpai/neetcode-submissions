class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        phone_map ={
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
            }
        
        return self._letterCombinations(digits, phone_map)
    
    def _letterCombinations(self, digits, phone_map):
        if len(digits) == 0:
            return [""]
        
        first_digit = digits[0]
        remaining_digits = self._letterCombinations(digits[1:], phone_map)

        result = []

        for letter in phone_map[first_digit]:
            for letters in remaining_digits:
                result.append(letter + letters)

        
        
        
        return result
                

        