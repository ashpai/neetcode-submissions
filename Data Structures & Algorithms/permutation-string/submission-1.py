class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        - edge conditions 
        - freq_map for smaller string
        - freq_map for window string
        - iterate with fixed window (len(s1)) and check if freq_map match 
        - if so, true
        - else false
        """
        if not s1 or not s2:
            return False
        
        if len(s1) > len(s2):
            return False
        

        def generate_sign(input: str) -> str:
            substring_map = [0 for i in range(26)]
            for char in input:
                substring_map[ord(char)-ord('a')] += 1

            signature ="#".join(map(str,substring_map))
            return signature

        start = 0
        k = len(s1)
        to_match = generate_sign(s1)

        while start + k <= len(s2):
            if generate_sign(s2[start:start+k]) == to_match:
                
                return True
            
            start += 1
        
        return False

        