class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        l = len(nums)
        dp = [1] * l
        res = 1
        for i in range(1, l):
            j = i-1
            while j > -1:
                if nums[j] < nums[i]:
                    dp[i] = max(dp[j] + 1, dp[i])
                res = max(dp[i], res)
                j -= 1
                
        return res