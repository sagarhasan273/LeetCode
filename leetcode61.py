# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        c = 0
        temp = head
        while temp:
            c += 1
            temp = temp.next
            
        k = k % c if c else k
        while k != 0 and head:
            prev = head
            last = head.next
            while last and last.next:
                prev = prev.next
                last = last.next
            if last:
                last.next = head
                prev.next = None
                head = last
            k -= 1
        
        return head