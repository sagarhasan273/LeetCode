class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        rows = len(mat)
        old_hash_set = set({0})
        
        for i in range(rows):
            hash_set = set()
            max_val = None
            for elem in old_hash_set:
                for row_val in sorted(mat[i]):
                    if max_val is not None and elem + row_val >= max_val:
                        continue
                    
                    if max_val is None and elem + row_val >= target:
                        max_val = elem + row_val
                        hash_set.add(max_val)
                    else:
                        hash_set.add(elem+row_val)
            old_hash_set = hash_set
        
        min_dif = float('inf')

        for elem in old_hash_set:
            if min_dif > abs(target-elem):
                min_dif = abs(target-elem)

        return min_dif