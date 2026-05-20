# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2: return None
        
        if not list1: return list2

        if not list2: return list1

        start = ListNode(0)
        result = start

        while list1 and list2:
            if list1.val <= list2.val:
                result.next = list1
                list1=list1.next
            else:
                result.next = list2
                list2=list2.next
            result = result.next
        
        result.next = list1 if list1 else list2
        
        start = start.next
        return start
        

        
