class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result =set()

        def dfs(current_path, current_sum) -> None:
            if current_sum > target:
                return 
            if current_sum == target:
                if tuple(current_path) not in result:
                    result.add(tuple(sorted(current_path[:])))
                return
            
            for num in nums:
                current_path.append(num)
                dfs(current_path, current_sum + num)
                current_path.pop()
        dfs([], 0)
        return [list(item) for item in result]
        