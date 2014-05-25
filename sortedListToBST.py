'''
Created on May 18, 2014

@author: zhouguangyi2009
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # @param head, a list node
    # @return a tree node
    def sortedListToBST(self, head):
        if head == None:
            return None
        else:
            index = 0
            node = head
            while node != None:
                index += 1
                node = node.next
        return self.sortedList(head, 0, index-1)
    
    def sortedList(self, head, start, end):
        print end
        if start >= end:
            return None
        mid = int ( (start + end)/2 )
        
        left = self.sortedList(head, 0, mid)
        print '%mid', mid
        print '%start', start     
        print head.val
        parent = TreeNode( head.val )
        parent.left = left
        head = head.next
        parent.right = self.sortedList(head, mid, end)
        print '%mid', mid
        print '%end', end
        return parent
node1 = ListNode(-1)
node2 = ListNode(0)
node3 = ListNode(2)
node4 = ListNode(3)
node1.next = node2
node2.next = node3
node3.next = node4
print Solution().sortedListToBST(node1).val