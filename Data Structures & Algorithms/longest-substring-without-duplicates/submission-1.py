class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}

        start = 0
        max_length = 0

        for end in range(len(s)):
            
            if s[end] in seen and seen[s[end]] >= start:
                start = seen[s[end]] + 1
            else:
                max_length = max(max_length, end-start+1)
                
            seen[s[end]] = end
        return max_length




        