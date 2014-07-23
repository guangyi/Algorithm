'''
Created on May 28, 2014

@author: zhouguangyi2009
'''
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    
    # Iterative solution
    def flattenIt(self, root):
        if root == None: return
        stack = []
        head = root
        while len(stack) != 0 or root != None:
            if root != None:
                stack.append(root)
                root = root.left
            else: # root == None
                root = stack.pop()
                left = root.left
                right = root.right
                if left:
                    root.right = left
                    root.left = None
                    if right:
                        while left.right != None:
                            left = left.right
                        left.right = right           
                root = right
        return head
    
    # recursion solution                   
    def flatten(self, root):
        if root == None: return
        left = self.flatten(root.left)
        right = self.flatten(root.right)
        if left != None: 
            root.right = left
            root.left = None
            if right != None:
                while left.right != None:
                    left = left.right
                left.right = right
                left.left = None
        return root
    
    # No while loop to find the last node of left tree Recursion Solution
    def flatten3(self, root):
        if root == None: return None
        rightmostOfLeft = self.flatten(root.left)
        rightmostOfRight = self.flatten(root.right)
        right = root.right
        if root.left != None: 
            root.right = root.left
            root.left = None
            if right != None:
                rightmostOfLeft.right = right
        if rightmostOfRight:  return rightmostOfRight
        elif rightmostOfLeft: return rightmostOfLeft
        else: return root
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
rot =  Solution().flattenIt(root)
#rot =  Solution().flatten2(root)

while rot != None:
    print rot.val
    print rot.left
    rot = rot.right