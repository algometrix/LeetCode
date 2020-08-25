# Definition for singly-linked list.
# class ListNode:
#     def _init_(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, node, next_node):
        if next_node is None:
            return node
        
        if next_node.next is None:
            node.next = next_node.next
            next_node.next = node
            node = next_node
            return node
        
        else:
            node.next = self.swapNodes(node.next.next, next_node.next.next)
            next_node.next = node
            return next_node
            
            
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        
        head = self.swapNodes(head, head.next)
        return head