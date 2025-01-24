import math

class Solution0(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        def getMerged(nums1, nums2):
            i = len(nums1)-1
            j = len(nums2)-1
            n = len(nums1) + len(nums2)
            arr = [0] * n
            
            k = n -1

            while i >= 0 and j >=0:
                if nums1[i] > nums2[j]:
                    arr[k] = nums1[i]
                    i -=1
                else:
                    arr[k] = nums2[j]
                    j-=1
                k -= 1

            while i >= 0:
                arr[k] = nums1[i]
                i -=1
                k -= 1

            while j >= 0:
                arr[k] = nums2[j]
                j -=1
                k -= 1

            return arr
        
        arr = getMerged(nums1, nums2)
        #Lets to binary search to find the median

        n = len(arr)
        ans = 0.0
        mid = n //2

        if n%2 == 0 :
            ans = (arr[mid] + arr[mid-1]) / 2.0 
        else:
            ans = arr[mid]
            
        return ans
        
            
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        A, B = nums1, nums2
        total =  len(A) + len(B)
        half = total //2

        if len(B) < len(A):
            A, B = B, A

        l, r = 0, len(A)-1

        while True:
            i = ( l + r ) // 2  #A
            j = half - i  - 2      #B

            #Managin edge cases
            pALeft = A[i] if i >= 0 else float("-inf")
            pARight = A[i + 1] if (i + 1) < len(A) else float("inf")
            pBLeft = B[j] if j >= 0 else float("-inf")
            pBRight = B[j + 1] if (j + 1) < len(B) else float("inf")

            if pALeft <= pBRight  and pBLeft <= pARight:
                #odd
                if total % 2:
                    return min(pARight, pBRight)
                else:
                #even
                    return (max(pALeft, pBLeft) + min(pARight, pBRight) ) / 2
            elif pALeft > pBRight:
                r = i - 1
            else:
                l = i + 1


        



#nums1 = [1,3, 4]
#nums2 = [2, 5, 7]

#nums1 = [1,3]
#nums2 = [2,4]

nums1 = [1,2,3,4,5]
nums2 = [6,7,8,9,10,11,12,13,14,15,16,17]

sl = Solution()
print(sl.findMedianSortedArrays(nums1, nums2))