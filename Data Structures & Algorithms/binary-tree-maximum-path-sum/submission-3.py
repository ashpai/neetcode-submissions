# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float('-inf')
        def dfs(root: Optional[TreeNode]):
            nonlocal max_sum
            if not root:
                return 0
            max_left = dfs(root.left)
            max_right = dfs(root.right)
            max_sum = max(max_sum, max_left + max_right + root.val,max_left + root.val,max_right + root.val, root.val)

            return max(root.val, root.val + max(max_left,max_right)) 
            

        dfs(root)
        return max_sum

        
        