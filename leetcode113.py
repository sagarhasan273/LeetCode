# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return root
        
        ans = []
        
        def dfs(node, res):
            if node.left:
                dfs(node.left,  res+[node.left.val])
            if node.right:
                dfs(node.right,  res+[node.right.val])
            else:
                if sum(res) == targetSum and not node.left and not node.right:
                    ans.append(res)
            
        dfs(root, [root.val])
        return ans