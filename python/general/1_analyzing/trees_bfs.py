from collections import deque
from typing import Optional
from pydantic import BaseModel

class TreeNode(BaseModel):
   val: int = 0
   left: Optional["TreeNode"] = None
   right: Optional["TreeNode"] = None

#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

##Root  
#      Level 1
root = TreeNode(val=1, 
        #Level 2 Left 
        left =TreeNode(
            val=5, 
            #Level 3  Left   
            left=TreeNode(
               val=7, 
               left=None,
               right=None
            ),
            #Level 3  Right
            right=TreeNode(
                val=9, 
                #Level 4  Left   
                left=TreeNode(
                    val=3, 
                    left=None,
                    right=None
                ),
                #Level 4  Right   
               right=None
            )
        ), 
        #Level 2 Right 
        right= TreeNode(
            val=8, 
            #Level 3 Left 
            left=None, 
            #Level 3 Right 
            right=TreeNode(
               val=10, 
               left=None,
               right=None
            )
        )
    )

print(root.model_dump_json(indent=2))


##Traverse the tree with a BFS

def print_each_level(root:TreeNode):
   queue = deque([root])

   while queue:
    nodes_in_level = len(queue)
  
    for _ in range(nodes_in_level):
        node = queue.popleft()
        print(node.val, end=" ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    print()

print_each_level(root)


      
      