class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        dp = [["X"] * cols for _ in range(rows)]

        def dfs(r, c, visited):
            if (r, c) in visited:
                return
            
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] == "X":
                return
            
            visited.add((r, c))
            dp[r][c] = "O"
            dfs(r+1, c, visited)
            dfs(r-1, c, visited)
            dfs(r, c+1, visited)
            dfs(r, c-1, visited)
            
        for c in range(cols):
            dfs(0, c, set())
            dfs(rows-1, c, set())
        
        for r in range(rows):
            dfs(r, 0, set())
            dfs(r, cols-1, set())
        
        for r in range(rows):
            for c in range(cols):
                board[r][c] = dp[r][c]
        