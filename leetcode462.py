class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums)%2 == 1:
            m = len(nums)//2
            total = 0
            for i in nums:
                total += abs(i - nums[m])
            return total
        else:
            m = (len(nums)//2) - 1
            m0 = m + 1
            totalm, totalm0 = 0, 0
            
            for i in nums:
                totalm += abs(i-nums[m])
                totalm0 += abs(i-nums[m0])
            
            return min(totalm, totalm0)
        