# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if not root:
            return result 
        
        q = deque([root])

        while q:
            level_size = len(q)

            level = []
            for _ in range(level_size):
                item = q.popleft()
                level.append(item.val)

                if item.left:
                    q.append(item.left)
                if item.right:
                    q.append(item.right)
            result.append(level)
        
        return result
        