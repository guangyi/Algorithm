'''
Created on May 28, 2014

@author: zhouguangyi2009
'''

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        if root == None:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        if left >= right:
            left += 1
        else: right += 1
        return max(left, right)