'''
Created on May 18, 2014

@author: zhouguangyi2009
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, num):
        if len(num) == 0:
            return None
        root = self.sortedArray(num, 0, len(num)-1 )
        return root
    def sortedArray(self, num, start, end):
        if start > end:        
            return None
        mid = int( (start + end)/2 )
        root = TreeNode( num[mid] )
        root.left = self.sortedArray(num, start, mid-1)
        root.right = self.sortedArray(num, mid+1, end)
        return root

root = Solution().sortedArrayToBST([1,2, 3])
print root.val