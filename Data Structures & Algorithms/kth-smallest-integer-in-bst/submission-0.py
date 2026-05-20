# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from heapq import heapify, heappop, heappush
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result =[]
        heapq.heapify(result)
        def helper(root: Optional[TreeNode]) -> None:
            nonlocal result
            if not root:
                return
            heappush(result, root.val)
            helper(root.left)
            helper(root.right)
        helper(root)
        for i in range(k-1):
            heappop(result)
        return result[0] if len(result) > 0 else -1
        