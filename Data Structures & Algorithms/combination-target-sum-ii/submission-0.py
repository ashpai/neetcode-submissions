class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result =[]
        candidates.sort()
        def dfs(path, index, target):
            if target == 0:
                result.append(path[:])
                return
            if target < 0:
                return
            
            for i in range(index, len(candidates)):
                if candidates[i] > target:
                    break
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                 
                path.append(candidates[i])
                dfs(path, i+1, target - candidates[i])
                path.pop()
        dfs([], 0, target)
        return result
        