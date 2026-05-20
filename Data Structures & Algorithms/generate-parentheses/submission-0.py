class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result =[]
        def backtrack(current, open_count, close_count):
            # base case
            if close_count > open_count:
                return
            if open_count > n or close_count > n:
                return
            if len(current) == 2*n:
                result.append("".join(current))
                return
            
            current.append("(")
            backtrack(current, open_count+1, close_count)
            current.pop()
            current.append(")")
            backtrack(current, open_count, close_count+1)
            current.pop()
        backtrack([], 0, 0)
        return list(result)


        