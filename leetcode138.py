"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def __init__(self):
        self.hashMap = {None: None}
        
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        temp = head
        while temp:
            copy = Node(temp.val)
            self.hashMap[temp] = copy 
            temp = temp.next

        
        temp = head
        while temp:
            copy = self.hashMap[temp]
            copy.next = self.hashMap[temp.next]
            copy.random = self.hashMap[temp.random]
            temp = temp.next
        
        return self.hashMap[head]