# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        maxWidth = 0
        level = [(1, root)]
        while len(level) > 0:
            maxWidth = max(maxWidth, level[-1][0] - level[0][0] + 1)
            temp = []
            for current_level, node in level:
                for index, child in enumerate((node.left, node.right), 2 * current_level):
                    if child is not None:
                        temp.append((index, child))
                
            level = temp
        
        return maxWidth


        