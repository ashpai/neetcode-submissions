class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        result = []

        for string in strs:
            result.append(f"{len(string)}#{string}")
        return "".join(result)

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        
        i = j = 0


        """
        5#Hello5#World
        i = 0 j = 0 len = ""
        i = 1 j = 0 len = "5" -> j = 2 string = str[2:7]
        i = 7 j = 7 len = "5"
        """
        result = []
        
        while i < len(s):
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            result.append(s[i:j])
            i = j

        return result
            
