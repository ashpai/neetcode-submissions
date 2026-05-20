class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if len(s) == 1:
            return [[s]]
        if len(s) == 0:
            return [[]]
        result = []
        for i in range(len(s)):
            if self.is_palindrome(s[:i+1]):
                remainder = self.partition(s[i+1:]) # [[], []]
                for r in remainder:
                    result.append([s[:i+1], *r])
        return result


    def is_palindrome(self, s:str) -> bool:
        return s == s[::-1]     
        