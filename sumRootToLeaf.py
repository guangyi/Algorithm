'''
Created on Jul 25, 2014

@author: zhouguangyi2009
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    # sum4 and sum4 all works fine
    def sum3(self, root, resultSoFar):
        if root == None: return 0
        resultSoFar  = resultSoFar * 10 + root.val
        left = self.sum3(root.left, resultSoFar)
        right = self.sum3(root.right, resultSoFar)
        if left == 0 and right == 0: return resultSoFar
        return left + right
    
    def sum4(self, root, currSum):
        if root == None: return 0
        if root.left == None and root.right == None: return currSum * 10 + root.val
        left = self.sum4(root.left, currSum * 10 + root.val) if root.left else 0
        right = self.sum4(root.right, currSum * 10 + root.val) if root.right else 0
        return left + right
    
    def sumNumbers(self, root):
        return self.sum4(root, 0)
   
    
        

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
node1.right = node3
node4.right = node5
node5.left = node6
print Solution().sumNumbers(root)
