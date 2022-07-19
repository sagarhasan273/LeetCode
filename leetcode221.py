class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        ans = 0
        
        for i in range(rows):
            for j in range(cols):
                matrix[i][j] = int(matrix[i][j])
                
                if matrix[i][j] == 0:
                    continue
                    
                if i == 0 or j == 0:
                    ans = max(ans, matrix[i][j])
                    continue
                
                matrix[i][j] = 1 + min(int(matrix[i-1][j]), int(matrix[i-1][j-1]), int(matrix[i][j-1]))
                ans = max(ans, matrix[i][j])
        
        return ans*ans