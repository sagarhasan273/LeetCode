class Solution:
    def minPartitions(self, n: str) -> int:
        max_val = 0
        
        for char in n:
            max_val = max(int(char), max_val)
            
        return max_val