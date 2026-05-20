class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        print(intervals)

        result = []
        result.append(intervals[0])

        
        def can_merge(interval_a:List[int], interval_b:List[int])-> bool:
            return interval_a[1] >= interval_b[0]
        
        def merge(interval_a:List[int], interval_b:List[int]) -> List[int]:
            return [min(interval_a[0],interval_b[0]), max(interval_a[1],interval_b[1])]
        

        for i in range(1, len(intervals)):
            if can_merge(result[-1], intervals[i]):
                result[-1]= merge(result[-1], intervals[i])
            else:
                result.append(intervals[i])
        
        return result
        