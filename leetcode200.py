class Solution:
    
    def numIslands(self, grid: List[List[str]]) -> int:
        island = 0
        rows, cols = len(grid), len(grid[0])
        
        def bfs(r, c):
            q = collections.deque()
            q.append((r, c))
            while q:
                row, col = q.popleft()
                for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    r, c = row+dr, col+dc
                    if r in range(rows) and c in range(cols) and grid[r][c] == '1':
                        grid[r][c] = '#'
                        q.append((r, c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    island += 1
                    bfs(r, c)
        
        return island