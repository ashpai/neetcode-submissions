# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # def helper(l1: Optional[ListNode], l2: Optional[ListNode], carry =0)-> Optional[ListNode]:
        #     if not l1 and not l2 and carry == 0:
        #         return
        
        #     l1_val = l1.val if l1 else 0
        #     l2_val = l2.val if l2 else 0

        #     sum_val, carry = (l1_val + l2_val + carry) % 10, (l1_val + l2_val + carry) // 10
        #     sum_node = ListNode(sum_val)
        #     next_digit_node = helper(l1.next if l1 else None, l2.next if l2 else None, carry)

        #     sum_node.next = next_digit_node

        #     return sum_node
        # return helper(l1, l2)

        carry_ = 0
        curr = ListNode(0)
        dummy = curr

        while l1 or l2 or carry_:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            sum_, carry_ = (l1_val + l2_val + carry_) % 10, (l1_val + l2_val + carry_) // 10
            curr.next = ListNode(sum_)

            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummy.next




            
        