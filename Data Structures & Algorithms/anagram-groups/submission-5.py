class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            representation = self.get_representation(word)

            if representation not in groups:
                groups[representation] = []
            
            groups[representation].append(word)



        return list(groups.values())

 

    def get_representation(self, word: str) -> str:
        result = [0] * 26
        
        for index, value in enumerate(word):
            result[ord(value) - ord("a")] += 1


        return "#".join([str(item) for item in result])

        