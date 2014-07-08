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
    # @return a list of lists of integers
    def levelOrderBottom(self, root):
        if root == None:return []
        thisLevel = [root]
        result = []
        while len(thisLevel) != 0:
            nextLevel = []
            temp = []
            for node in thisLevel:
                if node.left: nextLevel.append(node.left)
                if node.right: nextLevel.append(node.right)
                temp.append(node.val)
            result.insert(0, temp) #bottom up store
            thisLevel = nextLevel
        return result