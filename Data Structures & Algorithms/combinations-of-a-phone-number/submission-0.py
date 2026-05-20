class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result =[]
        phone_mapping={
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }
        def dfs(index, current:List[str]):
            if index == len(digits):
                result.append(''.join(current))
                return
            
            for char in phone_mapping[digits[index]]:
                current.append(char)
                dfs(index +1, current)
                current.pop()
        if len(digits) == 0:
            return result
        dfs(0, [])
        return result
        