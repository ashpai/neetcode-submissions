class Solution:

    def encode(self, strs: List[str]) -> str:
        result = []

        for string in strs:
            result.append(f"{len(string)}#{string}")

        # print("".join(result))
        return "".join(result)

    def decode(self, s: str) -> List[str]:
        i = j = 0


        """
        5#Hello5#World
        i = 0 j = 0 len = ""
        i = 1 j = 0 len = "5" -> j = 2 string = str[2:7]
        i = 7 j = 7 len = "5"
        """
        length = ""
        result = []
        while i < len(s):
            if s[i].isdigit():
                length += s[i]
                i += 1
            if s[i] == '#':
                j = i + 1
                string = s[j: j + int(length)]
                result.append(string)
                
                i = j + int(length)
                j = i
                length = ""

        return result
            
