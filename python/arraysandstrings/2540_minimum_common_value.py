"""
2540. Minimum Common Value
Solved
Easy
Topics
Companies
Hint
Given two integer arrays nums1 and nums2, sorted in non-decreasing order, return the minimum integer common to both arrays. If there is no common integer amongst nums1 and nums2, return -1.

Note that an integer is said to be common to nums1 and nums2 if both arrays have at least one occurrence of that integer.

 

Example 1:

Input: nums1 = [1,2,3], nums2 = [2,4]
Output: 2
Explanation: The smallest element common to both arrays is 2, so we return 2.
Example 2:

Input: nums1 = [1,2,3,6], nums2 = [2,3,4,5]
Output: 2
Explanation: There are two common elements in the array 2 and 3 out of which 2 is the smallest, so 2 is returned.
"""


# first  try
def getCommon(self, nums1: List[int], nums2: List[int]) -> int:

        l = 0
        r = len(nums1) -1

        j = 0
        k = len(nums2) -1
        ans = -1

        while l <= r  and j <= k:
            if nums1[r-l] == nums2[k-j]:
                ans = nums1[r-l]
                j+=1
                l+1
            elif nums1[r-l] < nums2[k-j]:
                j += 1 
            elif nums2[k-j] < nums1[r-l]:
                l += 1
        return ans 
        
#second try
# class Solution:
def getCommon2(self, nums1: List[int], nums2: List[int]) -> int:
    l = 0
    r = len(nums1)

    j = 0
    k = len(nums2) 

    while l < r and j < k:
        if nums1[l] == nums2[j]:
            return nums1[l]
        elif nums1[l] < nums2[j]:
            l += 1 
        else:
            j += 1
    return -1         