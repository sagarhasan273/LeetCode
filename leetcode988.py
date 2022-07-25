# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        hashMap = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k', 11: 'l', 12: 'm', 13: 'n', 14: 'o', 15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u', 21: 'v', 22: 'w', 23: 'x', 24: 'y', 25: 'z'}
        
        res_s = ['~']
        
        def dfs(node, s):
            if not node:
                return
            
            s = hashMap[node.val] + s
            if not node.left and not node.right:
                res_s[0] = min(res_s[0], s)
                return
            
            dfs(node.left, s)
            dfs(node.right, s)
        
        dfs(root, "")
        return res_s[0]