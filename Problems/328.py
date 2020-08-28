# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        elif head.next is None:
            return head
        
        even = head.next
        odd = head
        last_odd, last_even = None, None
        current_node = head
        position = 0
        while current_node is not None:
            position += 1
            if position%2 == 0:
                last_even = current_node
            else:
                last_odd = current_node
            tmp = current_node.next
            if current_node.next is not None:
                current_node.next = current_node.next.next
                
            current_node = tmp
            
        last_odd.next = even
        return head
    
     
        