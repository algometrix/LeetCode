# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDepth(self, root):
        if root is None:
            return 0
        
        leftDepth = self.getDepth(root.left) + 1
        rightDepth = self.getDepth(root.right) + 1
        return max(leftDepth, rightDepth)
    
    def nodeBalanced(self, root):
        if root is None:
            return True
        
        leftResult = self.getDepth(root.left)
        rightResult = self.getDepth(root.right)
        diff = abs(leftResult - rightResult)
        return (diff == 0 or diff == 1) and self.nodeBalanced(root.left) and self.nodeBalanced(root.right)
    
    def isBalanced(self, root: TreeNode) -> bool:
        return self.nodeBalanced(root)
        
        