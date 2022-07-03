class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n == 1:
            return nums[0] if k % 2 == 0 else -1
        
        return max(nums[i] for i in range(min(n, k + 1)) if i != (k-1))