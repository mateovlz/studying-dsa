"""
42. Trapping Rain Water
Solved
Hard
Topics
Companies
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
 

Constraints:

n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105
"""

# TC O(n)  SC O(n)
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        rightMax=[0] * n
        leftMax= [0] * n
        minLR = []
        lMax, temp = 0, 0
        for i in range(n):
            lMax = max(lMax, temp)
            leftMax[i]= lMax
            temp = height[i]

        rMax, temp = 0, 0
        for i in range(n-1, -1, -1):
            rMax = max(rMax, temp)
            rightMax[i]= rMax
            temp = height[i]

        print(rightMax)
        print(leftMax)

        ans = 0 
        for i in range(n):
            pw = min(leftMax[i], rightMax[i]) - height[i]
            print(pw)
            if pw > 0:
                ans+= pw
        return ans
    
# TC O(n)  SC O(1)
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l = 0 
        r = len(height) - 1

        leftMax = height[l]
        rightMax = height[r]
        ans = 0
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                ans += leftMax - height[l] 
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                ans += rightMax - height[r] 
        return ans

# TC O(n)  SC O(1)
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:  # Handle edge case of empty array
            return 0
        n = len(height)
        l, r = 0, n-1
        leftMax, rightMax = height[0], height[n-1]
        ans = 0
        while l < r:

            if leftMax < rightMax:
                l+=1
                leftMax = max(leftMax, height[l])
                ans += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                ans += rightMax - height[r]

        return ans
                
                