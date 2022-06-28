class Solution:
    def minDeletions(self, s: str) -> int:
        hashMap, res = {}, 0
        
        for c in s:
            if c in hashMap.keys():
                hashMap[c] += 1
            else:
                hashMap[c] = 1
        
        f_arr = list(hashMap.values())
        f_arr.sort(reverse=True)
        
        f = f_arr[0]
        for i in range(len(f_arr)):
            if f_arr[i] <= f:
                f = f_arr[i] - 1
            else:
                v = f_arr[i]
                while v > f:
                    v -= 1
                    res += 1
                f = 0 if (v-1) < 0 else v - 1
        
        return res
                
                           
        
        