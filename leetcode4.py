class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(A) + len(B)
        height = total//2
        if len(A) > len(B):
            A, B = B, A
        
        left, right = 0, len(A)-1
        while True:
            i = (left+right)//2
            j = height - i - 2
            
            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")
            
            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)
                
                return (max(Aleft, Bleft) + min(Aright, Bright)) /2
            
            elif Aleft > Bright:
                right = i - 1
            else:
                left = i + 1