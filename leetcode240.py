class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        
        def helper(arr, left, right):
            while left <= right:
                mid = left + (right-left)//2
                
                if arr[mid] == target:
                    return True
                if arr[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            
            return False
        
        for row in range(rows):
            if helper(matrix[row], 0, cols-1):
                return True
        
        return False