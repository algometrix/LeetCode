# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = []
        resultRoot, resultNode, prevNode = None, None, None
        carry = 0
        _sum = 0
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        
        while l1 is not None or l2 is not None:
            _sum = l1.val + l2.val + carry
            carry = _sum // 10
            _sum = _sum % 10 
            result.append(_sum)
            resultNode = ListNode(val=_sum)
            if prevNode is not None:
                prevNode.next = resultNode
            else:
                resultRoot = resultNode
            prevNode = resultNode
            l1 = l1.next
            l2 = l2.next
            if l1 is not None or l2 is not None:
                l1 = l1 if l1 is not None else ListNode(val=0)
                l2 = l2 if l2 is not None else ListNode(val=0)
        
            
        if carry != 0:
            resultNode.next = ListNode(val=carry)
        return resultRoot
        