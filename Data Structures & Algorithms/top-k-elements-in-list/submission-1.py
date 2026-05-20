from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # o(nlogn), o(n)
        # return [value[0] for value in Counter(nums).most_common(k)]

        frequency = [[] for _ in range(len(nums)+1)]
        counts = Counter(nums)
        result =[]

        for num, freq in counts.items():
            frequency[freq].append(num)
        
        for i in range(len(frequency)-1, -1, -1):
            while k > 0 and len(frequency[i]) > 0 :
                result.append(frequency[i].pop())
                
                k -= 1
        return result

        
        