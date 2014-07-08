'''
Created on Jul 7, 2014

@author: zhouguangyi2009
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        p1 = l1
        p2 = l2
        head = prevNode = ListNode(0)
        carryBit = 0
        while p1 != None or p2 != None or carryBit != 0:
            val1 = val2 = 0
            if p1 != None:
                val1 = p1.val
                p1 = p1.next
            if p2 != None:
                val2 = p2.val
                p2 = p2.next
            val = val1 + val2 + carryBit
            newVal = val % 10
            carryBit = val / 10
            newNode = ListNode(newVal)
            prevNode.next = newNode
            prevNode = newNode
        return head.next

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