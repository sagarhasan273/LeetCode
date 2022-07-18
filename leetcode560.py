class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = {0:1}
        
        n = len(nums)
        ans, s = 0, 0
        for r in range(n):
            s += nums[r]
            if s-k in d:
                ans += d[s-k]
                        
            if s in d:
                d[s] += 1
            else:
                d[s] = 1
        
        return ans