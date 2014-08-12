'''
Created on Jul 7, 2014

@author: zhouguangyi2009
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution:
    def addTwoNumbers(self, l1, l2):
        return self.add_help(l1, l2, 0)
        
    def add_help(self, l1, l2, carry):
        if l1 == None and l2 == None:
            if carry != 0: return ListNode(carry)
            else: return None
        val1 = 0 if l1 == None else l1.val
        val2 = 0 if l2 == None else l2.val
        carry, digit = divmod(val1 + val2 + carry, 10)
        l1 = l1 if l1 == None else l1.next
        l2 = l2 if l2 == None else l2.next
        head = ListNode(digit)
        head.next = self.add_help(l1, l2, carry)
        return head

l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(5)

l4 = ListNode(4)
l5 = ListNode(5)
l6 = ListNode(6)

l1.next = l2
l2.next = l3
l4.next = l5
l5.next = l6

node = Solution().addTwoNumbers(l1, l4)
while node != None:
    print node.val
    node = node.next