class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        char_difference = [0] * 26

        for i in range(len(s)):
            char_difference[ord(s[i]) - ord('a')] += 1
            char_difference[ord(t[i]) - ord('a')] -= 1

        for i in range(len(char_difference)):
            if char_difference[i] != 0:
                return False

        return True


        