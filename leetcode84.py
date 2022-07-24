class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea, l = 0, len(heights)
        
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height*(i-index))
                start = index
            stack.append([start, h])
        
        for i, h in stack:
            maxArea = max(maxArea, h*(l-i))
            
        return maxArea