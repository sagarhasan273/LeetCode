# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        queue = [root]
        res = []
        while queue:
            if root.left and root.left not in res:
                root = root.left
                queue. append(root)
            elif root.right:
                p = queue.pop()
                res += [p]
                root = res[-1].right
                queue. append(root) 
            else:
                p = queue.pop()
                res += [p]
                if queue:
                    root = queue[-1]
                else:
                    break
 
        return res[k-1].val