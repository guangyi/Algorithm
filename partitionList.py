'''
Created on May 24, 2014

Partition List

@author: zhouguangyi2009
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        if head == None:
            return None
        else:
            # extra two list
            large = ListNode(0)
            small = ListNode(0)
            largeHead = large
            smallHead = small
            while head != None:
                if head.val < x:
                    small.next = head
                    small = small.next
                else:
                    large.next = head
                    large = large.next    
                head = head.next
            large.next = None
            small.next = largeHead.next
            return smallHead.next

node1 = ListNode(1)
node2 = ListNode(1)
node3 = ListNode(2)
node4 = ListNode(1)
node1.next = node2
node2.next = node3
node3.next = node4

res = Solution().partition(node1, 0)
print  res.val
print  res.next.val
print  res.next.next.val
print  res.next.next.next.val
print  res.next.next.next.next

res2 = Solution().partition(node3, 2)
print  res2.val
print  res2.next.val
print  res2.next.next

res3 = Solution().partition(node3, 3)
print  res3.val
print  res3.next.val
print  res3.next