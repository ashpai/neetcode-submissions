# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = float('-inf')
        def helper(root):
            nonlocal diameter
            if not root:
                return 0
            left = helper(root.left)
            right = helper(root.right)
            diameter = max(diameter, left + right)
            return 1 + max(left, right)
        helper(root)
        return diameter
        