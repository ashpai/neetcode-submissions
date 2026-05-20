class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        freq_count ={"A":3}, max = 3
        freq_count ={"A":1, "B":2 }, max = 5
        """
        start = 0
        freq_count = {}
        max_window = 0
        max_f = 0

        def other_count():
            # o(n)
            return sum(freq_count.values()) - max(freq_count.values())

        for end in range(len(s)):
            freq_count[s[end]] = freq_count.get(s[end],0) + 1 
            max_f = max(max_f, freq_count[s[end]])

            # while len(freq_count.keys()) > 1 and other_count() > k:
            while (end - start + 1) - max_f > k:
                # condition to shorten window
                freq_count[s[start]] -= 1
                if freq_count[s[start]] == 0:
                    del freq_count[s[start]]
                start += 1
            max_window = max(max_window, end - start + 1)
        return max_window
             



        