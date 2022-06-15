import sys


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_string = left = 0
        seen = {}
        
        for i, char in enumerate(s):
            if left <= seen.get(char, -1):
                left = seen[char] + 1
            else:
                longest_string = max(longest_string, i + 1 - left)               
            
            seen[char] = i
        return longest_string