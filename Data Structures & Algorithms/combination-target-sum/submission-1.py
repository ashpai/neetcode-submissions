class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result =[]
        seen = set()

        def dfs(current_path, current_sum) -> None:
            if current_sum > target:
                return 
            if current_sum == target and tuple(sorted(current_path)) not in seen:
                seen.add(tuple(sorted(current_path)))
                result.append(current_path[:])
                return
            
            for num in nums:
                current_path.append(num)
                dfs(current_path, current_sum + num)
                current_path.pop()
        dfs([], 0)
        return result