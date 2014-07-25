# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):
        # Both are None
        if p == q: return True
        if (p == None and q != None) or (p != None and q == None): return False
        # Both have node
        left = self.isSameTree(p.left, q.left)
        if left != True: return False
        right = self.isSameTree(p.right, q.right)
        if right != True: return False
        if p.val == q.val: return True
        return False