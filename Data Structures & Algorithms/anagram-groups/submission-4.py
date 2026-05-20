from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_grouping: Dict[str, List[str]] = {}
        # ana_grouping = defaultdict(list)

        
        def get_rep(word: str) -> str:
            result =[0] * 26
            for char in word:
                result[ord(char)-ord('a')]+=1
            return "#".join(map(str,result))

        
        for word in strs:
            print(get_rep(word))
            ana_grouping.setdefault(get_rep(word),[]).append(word) 

        return ana_grouping.values()

        