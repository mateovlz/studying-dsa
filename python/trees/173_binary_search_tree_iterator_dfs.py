"""
173. Binary Search Tree Iterator
Solved
Medium
Topics
Companies
Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):

BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the BST is given as part of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.
boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer, otherwise returns false.
int next() Moves the pointer to the right, then returns the number at the pointer.
Notice that by initializing the pointer to a non-existent smallest number, the first call to next() will return the smallest element in the BST.

You may assume that next() calls will always be valid. That is, there will be at least a next number in the in-order traversal when next() is called.

 

Example 1:


Input
["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
[[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []]
Output
[null, 3, 7, true, 9, true, 15, true, 20, false]

Explanation
BSTIterator bSTIterator = new BSTIterator([7, 3, 15, null, null, 9, 20]);
bSTIterator.next();    // return 3
bSTIterator.next();    // return 7
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 9
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 15
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 20
bSTIterator.hasNext(); // return False
 

Constraints:

The number of nodes in the tree is in the range [1, 105].
0 <= Node.val <= 106
At most 105 calls will be made to hasNext, and next.
 

Follow up:

Could you implement next() and hasNext() to run in average O(1) time and use O(h) memory, where h is the height of the tree?
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: Optional[TreeNode]
        """
        self.stack = []
        self.helper(root)

    def next(self):
        """
        :rtype: int
        """
        res = self.stack.pop()
        cur = res.right
        self.helper(cur)
        return res.val       

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.stack != []

    def helper(self, node):
        while node:
            self.stack.append(node)
            node = node.left
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: Optional[TreeNode]
        """
        self.tree = root
        

    def next(self):
        """
        :rtype: int
        """
        if not self.tree:
            return 0
        
        if self.tree.left:
            return self.helper(self.tree.left, self.tree, None)

        if self.tree.right:
            val = self.tree.val 
            self.tree = self.tree.right
            return val
            
        val = self.tree.val
        self.tree = None
        return val

        

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.tree:
            return True
        else:
            return False

    def helper(self, next_node, actual_node, before_node):
        if not next_node:
            before_node.left = None
            self.tree = before_node
            return actual_node.val

        return self.helper(next_node.left, next_node, actual_node)
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()