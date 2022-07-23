# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        que = deque([(1, root)])

        while que:
            level, node = que.popleft()
            if not node.left and not node.right:
                return level
            
            if node.left:
                que.append((level+1, node.left))
            if node.right:
                que.append((level+1, node.right))
        
        