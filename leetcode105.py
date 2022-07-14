# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def dfs(preorder, inorder):
            if preorder and inorder:
                node = TreeNode(preorder[0])
                i = inorder.index(preorder[0])
                node.left = dfs(preorder[1:i+1], inorder[:i])
                node.right = dfs(preorder[i+1:], inorder[i+1:])
                return node

            return None
        
        return dfs(preorder, inorder)