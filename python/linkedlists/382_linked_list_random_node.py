# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import random

class Solution(object):

    def __init__(self, head):
        """
        :type head: Optional[ListNode]
        """
        self.head = head
        

    def getRandom(self):
        """
        :rtype: int
        """
        curr = self.head
        res =0 
        x = 0

        while curr:
            x += 1 

            if random.randint(1, x) == 1:
                res = curr.val
            
            curr = curr.next

        return res
        
 

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()