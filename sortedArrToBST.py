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
        return self.sortedArray(0, len(num)-1, num)
         
    def sortedArray(self, start, end, num):
        if start > end:
            return
        mid = int( start + end )/2
        parent = TreeNode( num[mid] )
        parent.left = self.sortedArray(start, mid-1, num)
        parent.right = self.sortedArray(mid+1, end, num)
        return parent

root = Solution().sortedArrayToBST([1,2, 3])
print root.val