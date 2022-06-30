class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == '' or len(t) > len(s): return ""
        
        window_map, t_map = {}, {}
        
        for i in range(len(t)):
            if t[i] not in window_map.keys():
                t_map[t[i]] = 0
            window_map[t[i]] = 0
            t_map[t[i]] += 1
        
        l = r = 0
        have, need, res, size = 0, len(window_map.keys()), [-1, -1], 9999999
        while r < len(s):
            if s[r] in window_map.keys():
                window_map[s[r]] += 1
                if window_map[s[r]] == t_map[s[r]]:
                    have += 1
            
            while have == need:
                if size > (r - l + 1):
                    res = [l, r]
                    size = (r - l + 1)
                    
                if s[l] not in window_map.keys():
                    l += 1
                    continue
                    
                window_map[s[l]] -= 1
                if window_map[s[l]] < t_map[s[l]]:
                    have -= 1
                l += 1
            r += 1
            
        return s[res[0]:res[1]+1] if res != [-1, -1] else ""