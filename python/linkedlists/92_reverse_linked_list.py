# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
     def __str__(self):
        return  str(self.val)

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        # Empty list
        if not head:
            return None
        
        #Move the two pointer until they reach starting point
        curr= head
        prev = None
        while left > 1:
            prev = curr
            curr = curr.next
            left -= 1
            right -= 1
            
        print(prev)
        print(curr)
        #The two pointer that will fix the final connections
        tail = curr
        con = prev
        
        #Iteratively reverse the nodes from right to left
        while right:
            third = curr.next
            curr.next = prev
            prev = curr
            curr = third
            right -=1
            
        print("other part")   
        print(prev)
        
        #adjuts the final connections
        if con:
            con.next = prev
        else:
            head = prev
            
        tail.next = curr
        
        return head

mynodes = ListNode(1,ListNode(2,ListNode(3, ListNode(4, ListNode(5,None)))))

solu = Solution()

print(solu.reverseBetween(mynodes, 2, 4))


    
            
        


        