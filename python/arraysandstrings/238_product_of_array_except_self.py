"""
238. Product of Array Except Self
Medium
Topics
Companies
Hint
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
"""
#working but not for all the cases when you add a 0 it breaks
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # I assume the first that comes to mind is
        # to iterate all the elements and get the total product
        # then iterate again a divide the ith value of each item
        total_product  = 1
        n  = len(nums)
        for i in range(n):
            total_product *= nums[i]

        ans = [0] * n
        for i in range(n):
            ans[i] = total_product // (nums[i] if nums[i] != 0 else 1)
        return ans        
        
        
        # build a prefix array with the product of a
        

# TC o(n)  SC 0(n)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix = [nums[0]]
        n = len(nums)
        ans = [0] * n
        suffix = [0] * (n)
        suffix[-1] = nums[-1]

        #building prefix ans suffix 

        for i in range(1, n):
            r_i = (n - 1) - i
            prefix.append(nums[i] * prefix[-1])
            suffix[r_i]= nums[r_i] * suffix[(r_i) + 1]


        #obtaining ith value    
        for i in range(n):
            left = 1
            right =1
            
            if (i - 1) >= 0:
                left = prefix[i - 1]
            if (i + 1) < n:
                right = suffix[i + 1]
            
            ans[i] = left * right
        
        return ans


# Using right culmulative variable to replace the prefix product
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        ans = [0] * n
        suffix = [0] * (n)
        suffix[-1] = nums[-1]

        #building prefix ans suffix 

        for i in range(1, n):
            r_i = (n - 1) - i
            suffix[r_i]= nums[r_i] * suffix[(r_i) + 1]


        #obtaining ith value    
        left = 1
        right = 1
        for i in range(n):
            r_i = n - i
            
            if (i - 1) >= 0:
                left *= nums[i - 1]
            if r_i < n:
                right *= nums[r_i]
            
            print(left, right)
            
            ans[i] = left * right
        
        return ans

        
#Best Solution 
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []
        #building prefix ans suffix 
        left = 1
        for i in range(n):
            ans.append(left)
            left *= nums[i]

        #obtaining ith value    
        right = 1
        for i in range(n-1, -1, -1):
            #         left  x right
            ans[i] = ans[i] * right
            right *= nums[i]
        
        return ans