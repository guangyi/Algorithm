'''
Created on Aug 1, 2014

@author: zhouguangyi2009
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        if head == None: return
        p = head
        if p.next == None: return head
        else: head = p.next
        while p != None and p.next != None:
            temp = p.next.next
            p.next.next = p
            p.next = temp
            p = temp
        return head

def pri(node):
    while node != None:
        print node.val
        node = node.next
        
head = ListNode(0)
l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)
l6 = ListNode(6)
head.next = l1

#l1.next = l2

l3.next = l4
l4.next = l5
l5.next = l6


h1 = Solution().swapPairs(head)
h2 = Solution().swapPairs(l3)
pri(h1)
pri(h2)


