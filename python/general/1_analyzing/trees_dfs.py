



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

print("#TREE InOrder")
def traverse_inorder(node):
    if not node:
        return 0
    
    
    traverse_inorder(node.left)
    print(node.val, end=" ")
    traverse_inorder(node.right)
    print()
    
    return 0

traverse_inorder(root)
   
print("#TREE PreOrder")
def traverse_preorder(node):
    if not node:
        return 0
    
    print(node.val, end=" ")
    traverse_preorder(node.left)
    traverse_preorder(node.right)
    print()
    return 

traverse_preorder(root)

print("#TREE Postorder")
def traverse_postorder(node):
    if not node:
        return 0
    print()
    traverse_postorder(node.left)
    traverse_postorder(node.right)
    print(node.val, end=" ")

    return 

traverse_postorder(root)


   