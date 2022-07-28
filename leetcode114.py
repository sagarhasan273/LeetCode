class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        def dfs(root):
            if root.right:
                return dfs(root.right)
            return root
            
        while root:
            if root.left:
                rightMost = dfs(root.left)
                nextRight = root.right
                root.right = root.left
                root.left = None
                rightMost.right = nextRight
            
            root = root.right