class Solution:
    def minWindow(self, s: str, t: str) -> str:
        result = ""
        min_size = float('inf')
        if len(t) > len(s):
            return result
        
        start = 0
        map_t, map_s = {}, {}
        for letter in t:
            map_t[letter] = 1 + map_t.get(letter, 0)

        for end in range(len(s)):
            map_s[s[end]] = 1 + map_s.get(s[end], 0)

            while all(c in map_s and map_s[c] >= map_t[c] for c in map_t): # not sure if this will work
                if end - start + 1 < min_size:
                    result = s[start:end+1] 
                    min_size = end - start +1 
                map_s[s[start]] -= 1
                if map_s[s[start]] == 0:
                    del map_s[s[start]]
                start += 1
        return result 
