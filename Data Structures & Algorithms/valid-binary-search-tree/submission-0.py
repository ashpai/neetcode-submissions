# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(root: Optional[TreeNode], min_value:int, max_value:int) -> bool:
            if not root:
                return True
            
            # valid range for the children
            isValidLeft = helper(root.left, min_value, root.val)
            isValidRight = helper(root.right, root.val, max_value)
            
            if (root.val < max_value and root.val > min_value) and isValidLeft and isValidRight:
                return True
            
            return False
        return helper(root, float('-inf'), float('inf'))
        