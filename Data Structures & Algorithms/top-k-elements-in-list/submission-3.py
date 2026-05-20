from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # frequency_map = Counter(nums)
        

        # heap = []

        # for key, value in frequency_map.items():
        #     heapq.heappush(heap, (value, key))

        #     if len(heap) > k:
        #         heapq.heappop(heap)

        # return [item[1] for item in heap]
        frequency_map = Counter(nums)

        fre_count = [[] for _ in  range(len(nums) + 1)]

        for key, value in frequency_map.items():
            fre_count[value].append(key)

        result = []
        
        for i in range(len(fre_count) -1, 0, -1):
            for num in fre_count[i]:
                result.append(num)
                
                if len(result) == k:
                    return result

        return result
        