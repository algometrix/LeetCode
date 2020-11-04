# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        queue = [(root, 1)]
        result = []
        if root is not None:
            result.append([root.val])
        else:
            return []
        while len(queue) > 0:
            temp = []
            for node, level in queue:
                for child in (node.left, node.right):
                    if child:
                        print(child.val)
                        temp.append((child, level + 1))
            print()
            #print(temp)
            if level % 2 == 0:
                result.append([ n[0].val for n in temp])
            else:
                result.append([ n[0].val for n in temp[::-1]])
            
            queue = temp[::]
        
        #print(result)
        return result[:-1]