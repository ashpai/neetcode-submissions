# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0
        def helper(root):
            nonlocal max_diameter
            if not root:
                return -1
            
            left_arm = 1 + helper(root.left)
            right_arm = 1 + helper(root.right)

            max_diameter = max(max_diameter, left_arm + right_arm)

            return max(left_arm, right_arm)
        
        helper(root)
        return max_diameter
        