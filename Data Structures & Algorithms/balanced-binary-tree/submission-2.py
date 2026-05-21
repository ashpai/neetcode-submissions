# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(root) -> tuple[int, bool]:
            if not root:
                return (-1, True)

            left_height, left_balanced = helper(root.left)
            right_height, right_balanced = helper(root.right)

            is_balanced = True
            if abs(left_height - right_height) > 1 or not left_balanced or not right_balanced:
                is_balanced = False
        
            return (1 + max(left_height, right_height), is_balanced)

        _, balanced = helper(root)
        return balanced
        