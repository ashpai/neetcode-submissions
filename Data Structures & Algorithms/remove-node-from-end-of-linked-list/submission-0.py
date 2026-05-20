# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Create a dummy node to handle head deletion
        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy
        
        # Advance fast by n steps
        for _ in range(n):
            if not fast:
                return head  # Invalid n, return original list
            fast = fast.next
        
        # Move both pointers until fast reaches the end
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        # Remove the nth node from end
        slow.next = slow.next.next
        
        return dummy.next