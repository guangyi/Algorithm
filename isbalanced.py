'''
Created on May 17, 2014

@author: zhouguangyi2009
'''
class tree():
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        if root == None: return True
        else:
            maxHeight = self.isBalance(root)
            print maxHeight
            if maxHeight != False:
                return True
            else: return False
    
    def isBalance(self, root):
        if root == None:
            return 0
        left = self.isBalance(root.left)
        right = self.isBalance(root.right)
        if left is False or right is False or abs(left - right) > 1: 
            print "false" 
            return False
        elif abs(left - right) <= 1:
            if left > right:
                left += 1
                return left
            else:
                right += 1
                return right

root = tree(1,None, None) 
print Solution().isBalanced(root)      