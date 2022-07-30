class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        num = deque(nums)
        l = len(nums)
        k = k % l
        for _ in range(k):
            num.appendleft(num.pop())

        for i in range(l):
            nums[i] = num[i]
