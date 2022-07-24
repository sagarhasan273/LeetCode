class Solution:
    def trap(self, height: List[int]) -> int:
        n, l_m, r_m = len(height), 0, 0
        ans = 0
        left, right = 0, n-1
        
        while left < right:
            if height[left] < height[right]:
                l_m = max(l_m, height[left])
                ans += l_m - height[left]
                left += 1
            else:
                r_m = max(r_m, height[right])
                ans += r_m - height[right]
                right -= 1
        
        return ans