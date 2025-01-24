
"""
55. Jump Game
Solved
Medium
Topics
Companies
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
 

Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 105
"""

#TC O(n) SC O(n) SC- due to the depth of the recursion stack
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        curr_i = n -1
        self.eva_i = n-2

        def helper(i):
            
            if i == 0:
                return True

            if self.eva_i < 0:
                return False

            jumps_need = i - self.eva_i 

            if nums[self.eva_i] >= jumps_need:
                self.eva_i -= 1
                return helper(i-jumps_need)
            else:
                self.eva_i -= 1
                return helper(i)
            return False

        if n == 0:
            return True
        
        return helper(curr_i)
    

#Greedy version thanks chatgpt
#TC O(n) SC O(1)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0
