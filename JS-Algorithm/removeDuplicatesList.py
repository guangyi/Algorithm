'''
Created on May 28, 2014

@author: zhouguangyi2009
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        # two pointer. if fast == slow
        # fast move to next
        # slow.next = slow.next.next
        if head == None or head.next == None: return head
        slow = head
        fast = head.next
        while fast != None:
            if slow.val == fast.val:
                fast = fast.next
                slow.next = slow.next.next
            else:
                fast = fast.next
                slow = slow.next
        return head