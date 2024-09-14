"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
"""

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)-1
        l = 0
        while l < len(nums)-1:
            r = l + 1
            if nums[l] == 0:
                while nums[r] == 0 and r < n:
                    r += 1
                nums[l] = nums[r]
                nums[r] = 0
            l+=1
            r+=1



        