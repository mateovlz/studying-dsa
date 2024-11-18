from typing import Optional
from pydantic import BaseModel

class ListNode(BaseModel):
     val: int = 0
     next : Optional["ListNode"] = None


class Solution(object):
    def reverse_linked_list(self, list):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """      

        curr = list
        prev = None

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev


solution = Solution()

#Input: list1 = [1,2,4]
#Output: [4,2,1]

list1 = ListNode(val=1, next=ListNode(val=2, next=ListNode(val=4)))
ans = solution.reverse_linked_list(list1)
print(ans.model_dump_json(indent=2))
