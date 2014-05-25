'''
Created on May 19, 2014

@author: zhouguangyi2009
'''
class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None
 
class Solution:
    def reverseList(self, node):
        if node == None:
            return 
        if node.next == None:
            return 
        temp = node.next
        self.reverseList(temp)
        node.next.next = node
        node.next= None
        node = temp
        #return node
        
        
        

node1 = ListNode(-1)
node2 = ListNode(0)
node3 = ListNode(2)
node4 = ListNode(3)
node1.next = node2
node2.next = node3
node3.next = node4
node = Solution().reverseList(node1)
print node4.next.val
print node3.next.val
print node2.next.val
print node.val