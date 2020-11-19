# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        queue = [root]
        while len(queue) > 0:
            level = []
            temp = []
            for node in queue:
                for child in (node.left, node.right):
                    if child:
                        temp.append(child)
                    
                    level.append(child.val if child is not None else None)
                    
            
            print(level)
            if level != level[::-1]:
                return False
            queue = temp[::]
        
        return True
        