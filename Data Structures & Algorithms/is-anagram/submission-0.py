class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not s and not t:
            return True
        if not s or not t:
            return False
        
        char_count_s = [0 for i in range(27)]
        char_count_t = [0 for i in range(27)]

        for char in s:
            char_count_s[ord(char)-ord('a')]+=1
        
        for char in t:
            char_count_t[ord(char)-ord('a')]+=1

        return char_count_s == char_count_t
        