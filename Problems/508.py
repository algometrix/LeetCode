# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getSum(self, root, memoryThingy):
        if root is None:
            return 0
        else:
            if hash(root) in memoryThingy.keys():
                return memoryThingy[hash(root)]
            else:
                subtree_sum = root.val + self.getSum(root.left, memoryThingy) + self.getSum(root.right, memoryThingy)
                memoryThingy[hash(root)] = subtree_sum
                return subtree_sum
            
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        from collections import Counter
        sum_list = []
        memoryThingy = {}
        if root is None:
            return []
        queue = [root]
        while queue:
            current_node = queue.pop(0)
            result = self.getSum(current_node, memoryThingy)
            sum_list.append(result)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
                
        
        _counter = Counter(sum_list)
        frequency = _counter.most_common(1)[0][1]
        return [ val for val, freq in _counter.most_common() if freq == frequency ] 
        