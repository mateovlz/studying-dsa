"""
2. Add Two Numbers
Solved
Medium
Topics
Companies
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
"""

from typing import Optional
from pydantic import BaseModel

class ListNode(BaseModel):
     val: int = 0
     next : Optional["ListNode"] = None
     #def __init__(self, val=0, next=None):
     #    self.val = val
     #    self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        du_iterate = dummy
        resi = 0
        curr1  = l1
        curr2 = l2

        while curr1 or curr2:
            num1 = 0
            num2 = 0
            ans = 0
       
            if curr1:
                num1 = curr1.val
                curr1 = curr1.next

            if curr2:
                num2 = curr2.val
                curr2 = curr2.next

            ans = num1 + num2 + resi
            temp = ans//10

            if temp != 0:
                resi = temp
                ans = ans%10
            else:
                resi = 0

            du_iterate.next = ListNode(ans)
            du_iterate = du_iterate.next

        if resi != 0 :
            du_iterate.next = ListNode(resi)
            du_iterate = du_iterate.next

        return dummy.next
    

#improvment on the carry/residual
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        du_iterate = dummy
        resi = 0
        curr1  = l1
        curr2 = l2

        while curr1 or curr2 or resi:
            num1 = 0
            num2 = 0
            ans = 0
       
            if curr1:
                num1 = curr1.val
                curr1 = curr1.next

            if curr2:
                num2 = curr2.val
                curr2 = curr2.next

            ans = num1 + num2 + resi
            temp = ans//10

            if temp != 0:
                resi = temp
                ans = ans%10
            else:
                resi = 0

            du_iterate.next = ListNode(ans)
            du_iterate = du_iterate.next


        return dummy.next