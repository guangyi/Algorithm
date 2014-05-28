'''
pre-order traversal. 
recursion way and iterative way
iterative: stack --> push root to stack --> tempNode = root --> add tempNode val to result --> push right node of tempNode 
--> push left node  of tempNode --> pop from stack as tempNode
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def __init__(self):
        self.result = []
    def preorderTraversal(self, root):
        if root == None:
            return []
        self.result.append(root.val)
        self.preorderTraversal(root.left)
        self.preorderTraversal(root.right)
        return self.result
    def iterative(self, root):
        if root == None:
            return []
        stack = [root]
        result = []
        tempNode = root
        while stack:
            result.append(tempNode.val)
            if tempNode.right:
                stack.append(tempNode.right)
            if tempNode.left:
                stack.append(tempNode.left)
            tempNode = stack.pop()
        return result