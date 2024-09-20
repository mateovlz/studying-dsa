"""
1302. Deepest Leaves Sum
Solved
Medium
Topics
Companies
Hint
Given the root of a binary tree, return the sum of values of its deepest leaves.
 

Example 1:


Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
Output: 15
Example 2:

Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 19
 
"""

from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.left)
            
            return max(left, right) + 1
        
        if not root:
            return 0
        
        queue = deque([root])
        ans = 0
        
        max_depth = dfs(root)
        level = 0
        while queue:
            nodes_in_level = len(queue)
            level += 1
            if level == max_depth:
                for node in queue:
                    ans += node.val
            for i in range(nodes_in_level):
                node = queue.popleft()
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return ans
                    
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
                
        next_level = deque([root])

        while next_level:
            curr_level = next_level
            next_level = deque()

            for node in curr_level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
        
        return sum( [ node.val for node in curr_level ] )
                            
            
        