

from typing import Optional
from pydantic import BaseModel

class ListNode(BaseModel):
     val: int = 0
     next : Optional["ListNode"] = None
     #def __init__(self, val=0, next=None):
     #    self.val = val
     #    self.next = next



myList = ListNode( 
    val=2,
    next= ListNode(
        val=3,
        next=ListNode(
             val=6,
             next=ListNode(
                  val=1,
                  next=ListNode(
                       val=5,
                       next=ListNode(
                            val=9,
                            next=None
                       )
                  )
             )
        )
    )
)

class Solution():

    def __init__(self, myList):
        self.myList = myList
        #self.print_list_o(self.myList)

    def print_list(self, list):
        print(list.model_dump_json(indent=1))
    
    def print_list_o(self, list):
        print()
        while list:
            print(list.val, end=" ")
            list = list.next

    def reverse_list(self, node:ListNode):
        self.print_list_o(node) 
        curr = node
        prev= None
        while curr:
            #We save the next node we are going to iterate
            next_node = curr.next
            #We update the current node to go towards the last node we saw
            curr.next = prev
            #We update the prev to have the node we are analyzing in this iteration
            prev = curr
            #We continue with the node that it was next at the beginning

            curr = next_node
            
        self.print_list_o(prev) 

    def find_middle_node(self, head:ListNode):
        
        slow = head
        fast = head
        print()
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        self.print_list_o(slow)
        


solution = Solution(myList)

solution.find_middle_node(myList)
solution.reverse_list(myList)






