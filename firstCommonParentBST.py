'''
Created on Jul 24, 2014

find the first common ancestor of a binary tree

@author: zhouguangyi2009
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution():
    def commonParentBST(self, root, a, b):
        minVal = min(a.val, b.val)
        maxVal = max(a.val, b.val)
        return self.commonBST(root, minVal, maxVal).val
    
    def commonBST(self, root, minVal, maxVal):
        if root == None: return
        if root.val > maxVal:
            return self.commonBST(root.left, minVal, maxVal)
        if root.val < minVal:
            return self.commonBST(root.right, minVal, maxVal)
        if root.val >= minVal and root.val <= maxVal:
            return root
    
root = TreeNode(0)
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
root.left = node1
root.right = node4
node1.left = node2
node4.left = node3
node4.right = node5
node5.left = node6

print Solution().commonParentBST(root, node3, node4)