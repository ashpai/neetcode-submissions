class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        char_count = [0 for i in range(27)]

        for i in range(len(s)):
            char_count[ord(s[i])-ord('a')]+=1
            char_count[ord(t[i])-ord('a')]-=1

        return True if all([char == 0 for char in char_count]) else False
        