'''
Created on May 28, 2014

Determine a linked list has loop or not

@author: zhouguangyi2009
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        if  head == None or head.next == None: return False
        slow  = head
        fast = head.next
        while slow != fast:
            if fast != None and fast.next != None:
                slow = slow.next
                fast = fast.next.next
            else:
                return False
        return True