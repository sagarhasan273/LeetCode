class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        memo = {}
        rows, cols = len(matrix), len(matrix[0])

        def dfs(i, j, prev):
            if i >= rows or i < 0 or j < 0 or j >= cols or matrix[i][j] <= prev:
                return 0

            if (i, j) in memo:
                return memo[(i, j)]
            re = 1
                
            for r, c in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                re = max(re, 1 + dfs(i+r, j+c, matrix[i][j]))
                
            memo[(i, j)] = re
            return re

        maxLen = 0
        for r in range(rows):
            for c in range(cols):
                maxLen = max(maxLen, dfs(r, c, -1))
        
        return maxLen
        