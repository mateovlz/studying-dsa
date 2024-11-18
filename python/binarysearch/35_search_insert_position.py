"""
35. Search Insert Position
Solved
Easy
Topics
Companies
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104
"""


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0 
        right = len(nums)

        while left < right:
            mid = (left + right) //2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                right = mid
            else:
                left = mid + 1
        return left
        




def test(arr, target):
    left =0 
    right = len(arr)

    while left <= right:
        mid = (left + right) // 2
        print(left, right, mid)
        if arr[mid] == target:
            print("found it", mid)
            return
        if arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return left

def test2(arr, target):
    left =0 
    right = len(arr)

    while left < right:
        mid = (left + right) // 2
        print(left, right, mid)
        if arr[mid] > target:
            right = mid 
        else:
            left = mid + 1

    return left

print(test2([1,3,5,6], 5))