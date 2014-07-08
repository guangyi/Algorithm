'''
Created on May 17, 2014

@author: zhouguangyi2009
'''
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
        height = self.isBalance(root)
        if height is False: # when height = 0, make sure it returns True
            return False
        return True
    def isBalance(self, root):
        # can't return True, cause 1 == True
        # the height of each node will be wrong
        if root == None: return 0
        left = self.isBalance(root.left)
        if left is False: return False
        right = self.isBalance(root.right)
        if right is False: return False 
        if abs(left - right) > 1: return False
        else: return max(left, right) + 1
    
root = tree(1,None, None) 
print Solution().isBalanced(root)      