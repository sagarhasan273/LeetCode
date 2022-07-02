class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = [0, 0]
        rows, cols = len(grid), len(grid[0])
        
        def dfs(r, c):
            if r not in range(rows) or c not in range(cols):
                return
            
            if grid[r][c] == 1:
                maxArea[1] += 1
                maxArea[0] = max(maxArea[0], maxArea[1])
                grid[r][c] = 2
                dfs(r+1, c)
                dfs(r-1, c)
                dfs(r, c+1)
                dfs(r, c-1)
            return 
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    maxArea[1] = 0
                    dfs(r, c)
        
        return maxArea[0]