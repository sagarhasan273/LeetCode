class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        rows = len(triangle)
        if rows == 1:
            return triangle[0][0]
        
        for r in range(1, rows):
            cols = r+1
            for c in range(cols):
                left = triangle[r-1][c-1] if c-1 >= 0 else triangle[r-1][c]
                right = triangle[r-1][c] if c+1 < cols else triangle[r-1][c-1]
                triangle[r][c] += min(left, right)
            
        return min(triangle[-1])