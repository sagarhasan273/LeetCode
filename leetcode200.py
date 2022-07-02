class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island = 0
        rows, cols = len(grid), len(grid[0])
        
        def dfs(r, c):
            if r not in range(rows) or c not in range(cols):
                return
            if grid[r][c] == '1':
                grid[r][c] = '#'
                dfs(r+1, c)
                dfs(r-1, c)
                dfs(r, c+1)
                dfs(r, c-1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    island += 1
                    dfs(r, c)
        
        return island