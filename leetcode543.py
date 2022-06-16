# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode], res=0) -> int:
      
        res = [0]
        def dfs(root):
            if not root:
                return -1
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            res[0] = max(res[0], 2+left+right)
            
            return 1 + max(left, right)
        
        return res[0] if dfs(root) else 0