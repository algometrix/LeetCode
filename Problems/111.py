# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def node_depth(self, node):
        if node is None:
            return 0
        elif node.left is None and node.right is None:
            return 1
        elif node.left is None:
            return self.node_depth(node.right) + 1
        elif node.right is None:
            return self.node_depth(node.left) + 1
        else:
            return min(self.node_depth(node.left), self.node_depth(node.right)) + 1
    
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        return self.node_depth(root)
    