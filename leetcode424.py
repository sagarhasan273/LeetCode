class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashMap = {}
        for i in s:
            hashMap[i] = 0
        
        l, r, res = 0, 0, 0
        while r < len(s):
            hashMap[s[r]] += 1
            if (r-l + 1) - max(hashMap.values()) <= k:
                res = (r-l + 1)
                r += 1
            else:
                hashMap[s[l]] -= 1
                l += 1
                r += 1
        
        return res