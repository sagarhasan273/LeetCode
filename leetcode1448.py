# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def helper(root, max_x):
            if not root:
                return 0
            left = helper(root.left, max(max_x, root.val))
            right = helper(root.right, max(max_x, root.val))
            if root.val >= max_x:
                return 1 + left + right
            return left + right
        
        return helper(root, root.val)