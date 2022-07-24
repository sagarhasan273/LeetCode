class Solution:
    def trap(self, height: List[int]) -> int:
        n, l_m, r_m = len(height), -float("inf"), -float("inf")
        left_max, right_max = [0]*n, [0]*n
        for i in range(n):
            l_m = max(l_m, height[i])
            left_max[i] = l_m
        
        for i in range(n-1, -1, -1):
            r_m = max(r_m, height[i])
            right_max[i] = r_m
        
        ans = 0
        for i in range(n):
            ans += min(left_max[i], right_max[i]) - height[i]
        
        return ans