# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def make_linked_list(l1, l2, rem):
            if l1 is None and l2 is None:
                if rem > 0:
                    return ListNode(rem)
                else:
                    return 
            if l1 is None:
                l1 = ListNode()
            if l2 is None:
                l2 = ListNode()
            return ListNode((l1.val+l2.val+rem)%10, make_linked_list(l1.next, l2.next, (l1.val+l2.val+rem)//10))
        
        return make_linked_list(l1, l2, 0)