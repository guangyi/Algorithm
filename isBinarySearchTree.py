'''
Created on May 20, 2014

Check if a binary tree is a binary search tree

@author: zhouguangyi2009
'''
import sys

class ListNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isValidBST(self, root):
        return self.isValid(root, -sys.maxint-1, sys.maxint)
    
    def isValid(self, root, start, end):
        if root == None:
            return True
        rootVal = root.val
        if rootVal <= start or rootVal > end:
            return False
        else:
            left = self.isValid(root.left, start, rootVal)
            right = self.isValid(root.right, rootVal, end)
            if left == False or right == False:
                return False
        return True
3,#,30,10,#,#,15,#,45
root = ListNode(3)
node2 = ListNode(30)
node3 = ListNode(10)
node4 = ListNode(15)
node5 = ListNode(45)
root.right = node2
node2.left = node3
node3.right = node4
node4.right = node5
print Solution().isValidBST(root)